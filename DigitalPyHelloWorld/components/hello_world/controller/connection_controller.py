"""This is Hello World component controller responsible for handling the connections"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.action_mapper import ActionMapper
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response

from digitalpy.core.main.controller import Controller
from digitalpy.core.network.domain.network_client import NetworkClient


class ConnectionController(Controller):
    """This is Hello World component controller responsible for handling the connections
    and disconnections of clients.
    """

    def __init__(self, request: 'Request', response: 'Response', sync_action_mapper: 'ActionMapper', configuration: 'Configuration'):
        super().__init__(request, response, sync_action_mapper, configuration)

    def initialize(self, request: 'Request', response: 'Response'):
        return super().initialize(request, response)

    def client_hello(self, client: NetworkClient):
        """Handle a new connection from a client.

        Args:
            client (NetworkClient): The client that connected.
        """
        self.execute_sub_action("Connection")
        self.response.set_value("client", client)
        self.response.set_value("message", "Hello Client! What is your name?")
        return self.response

    def client_goodbye(self, client: NetworkClient):
        """Handle a client disconnecting.

        Args:
            client (NetworkClient): The client that disconnected.
        """
        self.execute_sub_action("Disconnection")
        self.response.set_value("client", client)
        self.response.set_value("message", "Goodbye Client!")
        return self.response
