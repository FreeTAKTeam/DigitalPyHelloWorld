from sqlalchemy import Text, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING, List

from .health_base import HealthBase


class Health(HealthBase):
    """ this class represents the health table in the component database

    Args:
        id (int): the id of the user
        status (str): the status of the user
        service_id (str): the service id of the user
        protocol (str): the protocol of the user
    """

    __tablename__ = 'Health'
    oid = Column(Text, primary_key=True)

    id = Column(Integer)
    BloodPressure = Column(Text)
    BodyTemperature = Column(Integer)
    CaloriesBurned = Column(Integer)
    HeartRate = Column(Integer)
    SleepData = Column(Integer)
    StepsCount = Column(Integer)
    StressLevel = Column(Text)
    bodyOxygen = Column(Integer)

    def __repr__(self) -> str:
        return super().__repr__() + f"BloodPressure: {self.BloodPressure}, BodyTemperature: {self.BodyTemperature}, " \
                                    f"CaloriesBurned: {self.CaloriesBurned}, HeartRate: {self.HeartRate}, " \
                                    f"SleepData: {self.SleepData}, StepsCount: {self.StepsCount}, " \
                                    f"StressLevel: {self.StressLevel}, bodyOxygen: {self.bodyOxygen}"
