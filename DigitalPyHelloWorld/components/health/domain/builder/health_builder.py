from digitalpy.core.domain.builder import Builder
from ...configuration.health_constants import HEALTH
from ...domain.model.health import Health
from ...domain.model.contact import Contact


class HealthBuilder(Builder):
    """Builds a health object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: Health = None  # type: ignore

    def build_empty_object(self, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Builds a Health object"""
        self.request.set_value("object_class_name", "Health")

        configuration = config_loader.find_configuration(HEALTH)

        self.result = super()._create_model_object(
            configuration, extended_domain={"Health": Health, "Contact": Contact})

    def add_object_data(self, mapped_object: bytes):
        """adds the data from the mapped object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", mapped_object)
        self.execute_sub_action("deserialize")

    def get_result(self):
        """gets the result of the builder"""
        return self.result
