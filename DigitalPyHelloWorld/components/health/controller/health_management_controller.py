from typing import TYPE_CHECKING

from digitalpy.core.main.controller import Controller
from ..domain.builder.health_builder import HealthBuilder
from .health_persistence_controller import HealthPersistenceController

if TYPE_CHECKING:
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.impl.default_action_mapper import DefaultActionMapper
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response
    from digitalpy.core.domain.domain.network_client import NetworkClient


class HealthManagementController(Controller):

    def __init__(self, request: 'Request',
                 response: 'Response',
                 sync_action_mapper: 'DefaultActionMapper',
                 configuration: 'Configuration'):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.health_builder = HealthBuilder(request, response, sync_action_mapper, configuration)
        self.health_persistence_controller = HealthPersistenceController(
            request, response, sync_action_mapper, configuration)

    def initialize(self, request: 'Request', response: 'Response'):
        """This function is used to initialize the controller. 
        It is intiated by the service manager."""
        self.health_builder.initialize(request, response)
        return super().initialize(request, response)

    def create_health_post(self, client: 'NetworkClient', data: bytes, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""

        self.health_builder.build_empty_object(config_loader)
        self.health_builder.add_object_data(data)
        health_obj = self.health_builder.get_result()

        # save the health object to the database
        self.health_persistence_controller.save_health(health_obj)

        # list type as only lists are supported for this parameter
        self.response.set_value("message", [health_obj])
        self.response.set_value("recipients", [str(client.get_oid())])
        self.response.set_action("publish")

    def delete_health_delete(self, client: 'NetworkClient', data: bytes, config_loader, *args, **kwargs):
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""

        self.health_builder.build_empty_object(config_loader)
        self.health_builder.add_object_data(data)
        health_obj = self.health_builder.get_result()

        # delete the health object from the database
        self.health_persistence_controller.remove_health(health_obj)

        # list type as only lists are supported for this parameter
        self.response.set_value("message", [health_obj])
        self.response.set_value("recipients", [str(client.get_oid())])
        self.response.set_action("publish")

    def retrieve_health_get(self, client: 'NetworkClient', id: int, config_loader, *args, **kwargs):
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""
        # get the health object from the database
        health_obj = self.health_persistence_controller.get_health(id)

        # list type as only lists are supported for this parameter
        self.response.set_value("message", [health_obj])
        self.response.set_value("recipients", [str(client.get_oid())])
        self.response.set_action("publish")

    def update_health_put(self, client: 'NetworkClient', data: bytes, config_loader, *args, **kwargs):
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""

        self.health_builder.build_empty_object(config_loader)
        self.health_builder.add_object_data(data)
        health_obj = self.health_builder.get_result()

        # update the health object in the database
        self.health_persistence_controller.update_health(health_obj)

        # list type as only lists are supported for this parameter
        self.response.set_value("message", [health_obj])
        self.response.set_value("recipients", [str(client.get_oid())])
        self.response.set_action("publish")

    def list_health_get(self, client: 'NetworkClient', config_loader, *args, **kwargs):
        """This function is used to handle inbound messages from a service and send a
         response back to the service."""

        health_objs = self.health_persistence_controller.get_all_healths()

        # list type as only lists are supported for this parameter
        self.response.set_value("message", health_objs)
        self.response.set_value("recipients", [str(client.get_oid())])
        self.response.set_action("publish")
