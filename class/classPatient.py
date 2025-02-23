from typing import List
from classSchedule import Scheduling

class Patient:
    def __init__(self, name: str, phone_number: str, cpf: str):
        self.name = name
        self.phone_number = phone_number
        self.cpf = cpf
        schedule = List[Scheduling]

    def authenticate_cpf(self, cpf):
        pass
    
    def authenticate_phone(self, phone):
        pass



    #adicionar as proteções + - #
