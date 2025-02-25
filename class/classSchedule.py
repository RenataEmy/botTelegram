from datetime import date, time
from classPatient import Patient
from classService import Service

class Scheduling:
    def __init__(self, date: date, time: time, status: enumerate, patient: Patient, service: Service):
        self._date = date
        self._time = time
        self.status = enumerate
        self.__patient = Patient
        self.service = Service