class Patient:
    def __init__(self, patient_id: str, name: str, contact_details: str):
        # Validate details before creating the patient state
        self.validate_patient_details(patient_id, name, contact_details)

        self.__patient_id = patient_id
        self.__name = name
        self.__contact_details = contact_details

    def __str__(self):
        return f"Patient ID: {self.__patient_id}, Name: {self.__name}, Contact Details: {self.__contact_details}"

    def validate_patient_details(self, patient_id, name, contact_details):
        if not patient_id:
            raise ValueError("Invalid patient id")
        if not name:
            raise ValueError("Invalid name")
        if not contact_details:
            raise ValueError("Invalid contact details")

    def set_patient_id(self, patient_id):
        if not patient_id:
            raise ValueError("Invalid patient id")
        self.__patient_id = patient_id

    def set_name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.__name = name

    def set_contact_details(self, contact_details):
        if not contact_details:
            raise ValueError("Invalid contact details")
        self.__contact_details = contact_details

    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_contact_details(self):
        return self.__contact_details