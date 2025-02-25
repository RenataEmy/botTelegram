from classSpecialty import Specialty

class Doctor:
    def __init__(self, name: str, crm: str, specialty: Specialty):
        self.name_doctor = name
        self.__crm = crm
        self.specialty = Specialty