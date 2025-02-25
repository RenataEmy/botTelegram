from typing import List
from classDoctor import Doctor
from classService import Service

class Specialty:
    
    def __init__(self, name: str, doctor: Doctor):
        self.name_specialty = name
        self.doctor_responsible = doctor
        self.service = List[Service]


