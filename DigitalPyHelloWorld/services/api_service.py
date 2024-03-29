"""This is the TCPCoTServer module. It is used to accept messages and forward messages over tcp.
"""

import time
import traceback
from typing import List
from FreeTAKServer.core.cot_management.configuration.cot_management_constants import COT_FORMAT
from digitalpy.core.domain.domain.network_client import NetworkClient

from digitalpy.core.main.object_factory import ObjectFactory
from digitalpy.core.parsing.formatter import Formatter
from digitalpy.core.service_management.digitalpy_service import DigitalPyService, COMMAND_ACTION
from digitalpy.core.service_management.domain.service_status import ServiceStatus
from digitalpy.core.network.network_sync_interface import NetworkSyncInterface
from digitalpy.core.zmanager.request import Request
from digitalpy.core.main.impl.default_factory import DefaultFactory
from digitalpy.core.telemetry.tracing_provider import TracingProvider
from digitalpy.core.zmanager.response import Response
from digitalpy.core.service_management.domain.service_description import ServiceDescription


class ApiService(DigitalPyService):
    """This is the TCPCoTService class. It is used to accept messages and forward messages over tcp.
    """

    endpoints: list[str] = ["login", "CreateHealth", "ListHealth"]

    def __init__(self, service_id: str, subject_address: str, subject_port: int,  # pylint: disable=useless-super-delegation
                 subject_protocol: str, integration_manager_address: str,
                 integration_manager_port: int, integration_manager_protocol: str,
                 formatter: Formatter, network: NetworkSyncInterface, protocol: str,
                 service_desc: ServiceDescription):
        super().__init__(
            service_id, subject_address, subject_port, subject_protocol,
            integration_manager_address, integration_manager_port, integration_manager_protocol,
            formatter, network, protocol, service_desc)

    def event_loop(self):
        """This is the main event loop for the HelloService. It is intiated by the service manager.
        """
        super().event_loop()

    def handle_connection(self, client: NetworkClient, req: Request):
        super().handle_connection(client, req)
        req.set_context("api")
        req.set_format("pickled")
        req.set_value("source_format", self.protocol)
        req.set_action("authenticate")
        client: 'NetworkClient' = req.get_value("client")
        client.protocol = self.protocol
        client.service_id = self.service_id
        req.set_value("user_id", str(client.get_oid()))
        self.subject_send_request(req, self.protocol)

    def handle_inbound_message(self, message: Request):
        """This function is used to handle inbound messages from other services. 
        It is intiated by the event loop.
        """

        # TODO: discuss this with giu and see if we should move the to the action mapping system?
        if message.get_value("action") == "connection":
            self.handle_connection(message.get_value("client"), message)

        elif message.get_value("action") == "disconnection":
            self.handle_disconnection(message.get_value("client"), message)

        else:
            self.handle_api_message(message)

    def response_handler(self, responses: List[Response]):
        for response in responses:
            if response.get_action() == COMMAND_ACTION:
                self.handle_command(response)
            else:
                self.handle_response(response)

    def handle_api_message(self, message: Request):
        """this method is responsible for handling the case where a client sends a request.
        Args:
            message (request): the request message
        """
        message.set_context("api")
        message.set_format("pickled")
        message.set_value("source_format", self.protocol)
        message.set_action(message.get_value("url")+message.get_value("method"))
        self.subject_send_request(message, self.protocol)

    def handle_response(self, response: Response):
        self.network.send_response(response)

    def handle_exception(self, exception: Exception):
        """This function is used to handle exceptions that occur in the service. 
        It is intiated by the event loop.
        """
        if isinstance(exception, SystemExit):
            self.status = ServiceStatus.STOPPED
        else:
            traceback.print_exc()
            print("An exception occurred: " + str(exception))

    def start(self, object_factory: DefaultFactory, tracing_provider: TracingProvider,  # pylint: disable=useless-super-delegation
              host: str = "", port: int = 0,) -> None:
        """We override the start method to allow for the injection of the endpoints and handlers
        to the network interface.
        """
        ObjectFactory.configure(object_factory)
        self.tracer = tracing_provider.create_tracer(self.service_id)
        self.initialize_controllers()
        self.initialize_connections(self.protocol)

        self.network.intialize_network(host, port, self.endpoints, service_desc=self.service_desc)
        self.status = ServiceStatus.RUNNING
        self.execute_main_loop()
