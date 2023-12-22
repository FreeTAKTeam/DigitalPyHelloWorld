"""This is the HelloService module. It is used to say hello to the world. 
It is a simple example of a DigitalPyService."""

import time
import traceback

from digitalpy.core.parsing.formatter import Formatter
from digitalpy.core.service_management.digitalpy_service import DigitalPyService
from digitalpy.core.service_management.domain.service_status import ServiceStatus
from digitalpy.core.network.network_interface import NetworkInterface
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.main.impl.default_factory import DefaultFactory
from digitalpy.core.telemetry.tracing_provider import TracingProvider


class HelloService(DigitalPyService):
    """HelloService is a DigitalPyService that is used to say hello to the world. 
    It is a simple example of a DigitalPyService.
    """

    def __init__(self, service_id: str, subject_address: str, subject_port: int,  # pylint: disable=useless-super-delegation
                 subject_protocol: str, integration_manager_address: str,
                 integration_manager_port: int, integration_manager_protocol: str,
                 formatter: Formatter, network: NetworkInterface, protocol: str):
        super().__init__(
            service_id, subject_address, subject_port, subject_protocol,
            integration_manager_address, integration_manager_port, integration_manager_protocol,
            formatter, network, protocol)

    def event_loop(self):
        """This is the main event loop for the HelloService. It is intiated by the service manager.
        """
        super().event_loop()

        time.sleep(0.1)
        requests = self.network.service_connections()
        for request in requests:
            print("received "+str(request.get_value("data")) +
                  " from "+str(request.get_value("client").id))
            self.handle_inbound_message(request)

    def handle_inbound_message(self, message: Request):
        """This function is used to handle inbound messages from other services. 
        It is intiated by the event loop.
        """

        # TODO: discuss this with giu and see if we should move the to the action mapping system?
        if message.get_value("action") == "connection":
            self.handle_connection(message.get_value("client"), message)

        elif message.get_value("action") == "disconnection":
            self.handle_disconnection(message.get_value("client"), message)

        elif message.get_value("data"):
            self.handle_simple_hello(message)

    def handle_simple_hello(self, message: Request):
        """This function handles a simple hello message. 
        It is intiated by the inbound message handler.
        """
        message.set_context("Hello")
        message.set_action("ClientMessage")
        message.set_format("pickled")
        self.subject_send_request(message, self.protocol)

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
              host: str = "", port: int = 0) -> None:
        """This is the main running function for the HelloService. 
        It is intiated by the service manager.
        """
        super().start(object_factory, tracing_provider, host, port)
