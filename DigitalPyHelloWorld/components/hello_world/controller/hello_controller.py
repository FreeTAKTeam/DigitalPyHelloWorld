"""This file contains the HelloController class. This class is used to say hello to the world.
It performs simple operations based on input data and sends a response back to the service."""
from typing import TYPE_CHECKING

from digitalpy.core.main.controller import Controller
from ..domain.builder.hello_message_builder import HelloMessageBuilder

if TYPE_CHECKING:
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.action_mapper import ActionMapper
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response


class HelloController(Controller):
    """HelloController is a DigitalPyController that is used to say hello to the world. 
    By adding logic to the hello service"""

    def __init__(self, request: 'Request',
                 response: 'Response',
                 sync_action_mapper: 'ActionMapper',
                 configuration: 'Configuration'):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.hello_builder = HelloMessageBuilder(
            request, response, sync_action_mapper, configuration)

    def initialize(self, request: 'Request', response: 'Response'):
        """This function is used to initialize the controller. 
        It is intiated by the service manager."""
        self.hello_builder.initialize(request, response)
        return super().initialize(request, response)

    def client_message(self, data: str, *args, **kwargs):  # pylint: disable=unused-argument
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""

        self.hello_builder.build_empty_object(self.configuration)
        self.hello_builder.add_object_data(data)

        self.response.set_action("publish")
