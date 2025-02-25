class Patient:
    def __init__(self, name: str, phone_number: str, cpf: str):
        self.name_patient = name
        self.__phone_number = phone_number
        self.__cpf = cpf

    def authenticate_cpf(self, cpf):
        pass
    
    def authenticate_phone(self, phone):
        pass

