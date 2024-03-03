# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node


class Health(Node):
    def __init__(self, model_configuration, model, oid=None, node_type="health") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._BloodPressure: str = ""
        self._BodyTemperature: int = 0
        self._CaloriesBurned: int = 0
        self._ID: int = -1

    @property
    def BloodPressure(self) -> str:
        """Blood pressure represents a single instantaneous blood pressure
            reading as a string  with systolic pressure first a separator : and the
            diastolic pressure second 60:90"""
        return self._BloodPressure

    @BloodPressure.setter
    def BloodPressure(self, BloodPressure: str):
        if not isinstance(BloodPressure, str):
            raise TypeError("'BloodPressure' must be a string")
        self._BloodPressure = BloodPressure

    @property
    def BodyTemperature(self) -> int:
        """Body temperature a single instantaneous body temperature measurement
            in Celsius"""
        return self._BodyTemperature

    @BodyTemperature.setter
    def BodyTemperature(self, BodyTemperature: int):
        if not isinstance(BodyTemperature, int):
            raise TypeError("'BodyTemperature' must be a integer")
        self._BodyTemperature = BodyTemperature

    @property
    def CaloriesBurned(self) -> int:
        """Calories burned in the last 24 hours"""
        return self._CaloriesBurned

    @CaloriesBurned.setter
    def CaloriesBurned(self, CaloriesBurned: int):
        if not isinstance(CaloriesBurned, int):
            raise TypeError("'CaloriesBurned' must be a integer")
        self._CaloriesBurned = CaloriesBurned

    @property
    def HeartRate(self) -> int:
        """Heart rate represents a single instantaneous heart rate measurement
            in beats per minute"""
        return self._HeartRate

    @HeartRate.setter
    def HeartRate(self, HeartRate: int):
        if not isinstance(HeartRate, int):
            raise TypeError("'HeartRate' must be a integer")
        self._HeartRate = HeartRate

    @property
    def ID(self) -> int:
        """ID is a unique identifier for the health information"""
        return self._ID

    @ID.setter
    def ID(self, ID: str):
        if not isinstance(ID, int):
            raise TypeError("'ID' must be an int")
        if ID < 0:
            raise ValueError("'ID' must be a positive integer")
        self._ID = ID

    @property
    def SleepData(self) -> str:
        """Sleep data represents the number of hours slept in the last 24 hours"""
        return self._SleepData

    @SleepData.setter
    def SleepData(self, SleepData: str):
        if not isinstance(SleepData, str):
            raise TypeError("'SleepData' must be a string")
        self._SleepData = SleepData

    @property
    def StepsCount(self) -> int:
        """Steps taken in the last 24 hours"""
        return self._StepsCount

    @StepsCount.setter
    def StepsCount(self, StepsCount: int):
        if not isinstance(StepsCount, int):
            raise TypeError("'StepsCount' must be a integer")
        self._StepsCount = StepsCount

    @property
    def StressLevel(self) -> str:
        """Stress level represents a single instantaneous stress level measurement
            in beats per minute"""
        return self._StressLevel

    @StressLevel.setter
    def StressLevel(self, StressLevel: str):
        if not isinstance(StressLevel, str):
            raise TypeError("'StressLevel' must be a string")
        self._StressLevel = StressLevel

    @property
    def bodyOxygen(self) -> int:
        """Body oxygen represents a single instantaneous body oxygen measurement
            in percentage"""
        return self._bodyOxygen

    @bodyOxygen.setter
    def bodyOxygen(self, bodyOxygen: int):
        if not isinstance(bodyOxygen, int):
            raise TypeError("'bodyOxygen' must be a integer")
        self._bodyOxygen = bodyOxygen
