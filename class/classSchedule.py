from datetime import date, time
from classPatient import Patient
from classService import Service

class Scheduling:
    def __init__(self, date: date, time: time, status: enumerate, patient: Patient, service: Service):
        self.date = date
        self.time = time
        self.status = enumerate
        self.patient = Patient
        self.service = Service