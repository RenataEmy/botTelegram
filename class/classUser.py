from typing import List
from classSchedule import Scheduling
from classPatient import Patient

class User(Patient):
    def __init__(self, name: str, phone_number: str, cpf: str, id: str):
        super().__init__(name, phone_number, cpf)
        self.__id = id
        schedule = List[Scheduling]