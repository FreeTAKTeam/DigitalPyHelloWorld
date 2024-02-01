from typing import Union
from digitalpy.core.domain.builder import Builder
from ...configuration.health_constants import HEALTH
from ...domain.model.health import Health
from ...domain.model.contact import Contact
from ...persistence.health import Health as DBHealth


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

    def add_object_data(self, mapped_object: Union[bytes, DBHealth]):
        """adds the data from the mapped object to the Health object """
        if isinstance(mapped_object, bytes):
            self._add_json_object_data(mapped_object)

        elif isinstance(mapped_object, DBHealth):
            self._add_db_object_data(mapped_object)

    def _add_json_object_data(self, json_object: bytes):
        """adds the data from the json object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", json_object)
        self.execute_sub_action("deserialize")

    def _add_db_object_data(self, db_object: DBHealth):
        """adds the data from the db object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", db_object)
        self.result.BloodPressure = db_object.BloodPressure
        self.result.BodyTemperature = db_object.BodyTemperature
        self.result.CaloriesBurned = db_object.CaloriesBurned
        self.result.HeartRate = db_object.HeartRate
        self.result.StepsCount = db_object.StepsCount
        self.result.SleepData = db_object.SleepData
        self.result.StressLevel = db_object.StressLevel

    def get_result(self):
        """gets the result of the builder"""
        return self.result
