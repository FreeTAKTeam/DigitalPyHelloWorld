import time
import traceback

from digitalpy.core.parsing.formatter import Formatter
from digitalpy.core.service_management.digitalpy_service import DigitalPyService
from digitalpy.core.service_management.domain.service_status import ServiceStatus
from digitalpy.core.network.network_interface import NetworkInterface
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response

class HelloService(DigitalPyService):
    """HelloService is a DigitalPyService that is used to say hello to the world. It is a simple example of a DigitalPyService.
    """
    def __init__(self, service_id: str, subject_address: str, subject_port: int, subject_protocol: str, integration_manager_address: str, integration_manager_port: int, integration_manager_protocol: str, formatter: Formatter, network: NetworkInterface, protocol: str):
        super().__init__(service_id, subject_address, subject_port, subject_protocol,
                         integration_manager_address, integration_manager_port, integration_manager_protocol, formatter,
                         network, protocol
                         )

    def event_loop(self):
        """This is the main event loop for the HelloService. It is intiated by the service manager.
        """
        super().event_loop()

        time.sleep(0.1)
        responses = self.network.service_connections()
        for response in responses:
            print("received "+str(response.get_value("data"))+" from "+str(response.get_value("client").id))
    
    def handle_inbound_message(self, message: Request):
        self.subject_send_request(message, self.protocol)
    
    def handle_exception(self, exception: Exception):
        if isinstance(exception, SystemExit):
            self.status = ServiceStatus.STOPPED
        else:
            traceback.print_exc()
            print("An exception occurred: " + str(exception))

    def start(self, factory, tracing_provider, host, port):
        """This is the main running function for the HelloService. It is intiated by the service manager.
        """
        super().start(factory, tracing_provider, host, port)