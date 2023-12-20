import multiprocessing
from digitalpy.core.component_management.impl.default_facade import DefaultFacade
from digitalpy.core.zmanager.impl.async_action_mapper import AsyncActionMapper
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.main.object_factory import ObjectFactory
from digitalpy.core.network.domain.network_client import NetworkClient

from .domain.model.hello_client import HelloClient
from .controller.connection_controller import ConnectionController

from .configuration.hello_world_constants import (
    ACTION_MAPPING_PATH,
    LOGGING_CONFIGURATION_PATH,
    INTERNAL_ACTION_MAPPING_PATH,
    MANIFEST_PATH,
    CONFIGURATION_PATH_TEMPLATE,
    LOG_FILE_PATH
)

from . import base

class HelloWorld(DefaultFacade):
    """HelloComponent is a DefaultFacade that is used to say hello to the world. It is a simple example of a DefaultFacade.
    """

    def __init__(self, sync_action_mapper, request: Request, response: Response, configuration, action_mapper: AsyncActionMapper=None, tracing_provider_instance=None): # type: ignore
        super().__init__(
                # the path to the external action mapping
                action_mapping_path=str(ACTION_MAPPING_PATH),
                # the path to the internal action mapping
                internal_action_mapping_path=str(INTERNAL_ACTION_MAPPING_PATH),
                # the path to the logger configuration
                logger_configuration=str(LOGGING_CONFIGURATION_PATH),
                # the package containing the base classes
                base=base,
                # the general action mapper (passed by constructor)
                action_mapper=sync_action_mapper,
                # the request object (passed by constructor)
                request=request,
                # the response object (passed by constructor)
                response=response,
                # the configuration object (passed by constructor)
                configuration=configuration,
                # log file path
                log_file_path= LOG_FILE_PATH,
                # the tracing provider used
                tracing_provider_instance=tracing_provider_instance,
                # the template for the absolute path to the model object definitions
                configuration_path_template=CONFIGURATION_PATH_TEMPLATE,
                # the path to the manifest file
                manifest_path=str(MANIFEST_PATH),
            )
        self.connection_controller = ConnectionController(request, response, action_mapper, configuration)
        
    def initialize(self, request, response):
        self.connection_controller.initialize(request, response)
        return super().initialize(request, response)

    def execute(self, method):
        try:
            if hasattr(self, method):
                print("executing method "+method)
                getattr(self, method)(**self.request.get_values())
            else:
                self.request.set_value("logger", self.logger)
                self.request.set_value("config_loader", self.config_loader)
                self.request.set_value("tracer", self.tracer)
                response = self.execute_sub_action(self.request.get_action())
                self.response.set_values(response.get_values())
        except Exception as e:
            self.logger.fatal(str(e))

    @DefaultFacade.public
    def new_client(self, *args, **kwargs):
        """This method is used to handle a new client.
        """
        self.connection_controller.new_client(*args, **kwargs)

    @DefaultFacade.public
    def client_message(self, message: bytes, client: HelloClient):
        """This method is used to receive name updates sent by the client.
        """
        self.response.set_value("message", message)