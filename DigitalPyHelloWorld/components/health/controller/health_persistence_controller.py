from typing import TYPE_CHECKING
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# import tables in initialization order
from ..persistence.health import Health as DBHealth

from ..domain.model.health import Health

from digitalpy.core.main.controller import Controller
from ..persistence.health_base import HealthBase
from ..configuration.health_constants import DB_PATH
if TYPE_CHECKING:
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.action_mapper import ActionMapper


class HealthPersistenceController(Controller):
    """this class is responsible for handling the persistence of the Health
    component. It is responsible for creating, removing and retrieving
    healths from the IAM system.

    Args:
        request (Request): the request object
        response (Response): the response object
        sync_action_mapper (ActionMapper): the action mapper
        configuration (Configuration): the configuration object
    """

    def __init__(
        self,
        request: 'Request',
        response: 'Response',
        sync_action_mapper: 'ActionMapper',
        configuration: 'Configuration',
    ):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.ses = self.create_db_session()

    def create_db_session(self) -> Session:
        """open a new session in the database

        Returns:
            Session: the session connecting the db
        """
        engine = create_engine(DB_PATH)
        # create a configured "Session" class
        SessionClass = sessionmaker(bind=engine)

        HealthBase.metadata.create_all(engine)

        # create a Session
        return SessionClass()

    def save_health(self, health: Health, *args, **kwargs):
        """this function is responsible for creating a health in the Health system.

        Args:
            health (NetworkClient): the health to be created
        """
        if not isinstance(health, Health):
            raise TypeError("'health' must be an instance of NetworkClient")

        db_health = DBHealth()
        db_health.oid = str(health.get_oid())
        db_health.id = health.ID
        db_health.BloodPressure = health.BloodPressure
        db_health.BodyTemperature = health.BodyTemperature
        db_health.CaloriesBurned = health.CaloriesBurned
        db_health.HeartRate = health.HeartRate
        db_health.SleepData = health.SleepData
        db_health.StepsCount = health.StepsCount
        db_health.StressLevel = health.StressLevel
        db_health.bodyOxygen = health.bodyOxygen

        self.ses.add(db_health)
        self.ses.commit()

    def remove_health(self, health: Health, *args, **kwargs):
        """this function is responsible for removing a health from the component.

        Args:
            health (NetworkClient): the health to be removed
        """
        if not isinstance(health, Health):
            raise TypeError("'health' must be an instance of Health")
        health_db = self.get_health(health.ID)
        self.ses.delete(health_db)
        self.ses.commit()

    def get_health(self, health_id: int, *args, **kwargs) -> DBHealth:
        """this function is responsible for getting a health from the IAM
        system.

        Args:
            health_id (str): the id of the health to be retrieved

        Returns:
            Health: the health retrieved
        """
        if not isinstance(health_id, str):
            raise TypeError("'health_id' must be an instance of str")
        return self.ses.query(DBHealth).filter(DBHealth.id == health_id).first()

    def get_all_healths(self, *args, **kwargs) -> list[DBHealth]:
        """this function is responsible for getting all healths from the IAM
        system.

        Returns:
            list[Health]: a list of all healths
        """
        return self.ses.query(DBHealth).all()

    def update_health(self, health: Health, *args, **kwargs):
        """this function is responsible for updating a health in the IAM
        system.

        Args:
            health (Health): the health to be updated
        """
        if not isinstance(health, Health):
            raise TypeError("'health' must be an instance of Health")
        health_db = self.get_health(health.ID)
        health_db.id = health.ID
        health_db.BloodPressure = health.BloodPressure
        health_db.BodyTemperature = health.BodyTemperature
        health_db.CaloriesBurned = health.CaloriesBurned
        health_db.HeartRate = health.HeartRate
        health_db.SleepData = health.SleepData
        health_db.StepsCount = health.StepsCount
        health_db.StressLevel = health.StressLevel
        health_db.bodyOxygen = health.bodyOxygen
        self.ses.commit()

    def __getstate__(self) -> object:
        state: dict = super().__getstate__()  # type: ignore
        if "ses" in state:
            del state["ses"]
        return state

    def __setstate__(self, state: dict) -> None:
        self.__dict__.update(state)
        self.ses = self.create_db_session()
