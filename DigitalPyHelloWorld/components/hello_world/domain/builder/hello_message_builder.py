"""This module contains the HelloMessageBuilder class for building hello messages instances"""
from digitalpy.core.domain.builder import Builder
from ...configuration.hello_world_constants import SIMPLE_HELLO_MESSAGE
from ..model.hello_message import HelloMessage


class HelloMessageBuilder(Builder):
    """Builds a hello message object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: HelloMessage = None  # type: ignore

    def build_empty_object(self, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Builds a HelloMessage object"""
        self.request.set_value("object_class_name", "MissionChangeRecord")

        configuration = config_loader.find_configuration(SIMPLE_HELLO_MESSAGE)

        self.result = super()._create_model_object(
            configuration, extended_domain={"HelloMessage": HelloMessage})

    def add_object_data(self, mapped_object: str):
        """adds the data from the mapped object to the HelloMessage object """
        self.result.message = mapped_object

    def get_result(self):
        """gets the result of the builder"""
        return self.result
