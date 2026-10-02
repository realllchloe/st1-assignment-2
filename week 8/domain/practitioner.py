from datetime import datetime


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        # Validate details before creating the practitioner state
        self.validate_practitioner_details(practitioner_id, name, specialty)

        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__specialty = specialty
        # Stores available appointment time slots
        self.__availability = []

    def __str__(self):
        return (f"Practitioner ID: {self.__practitioner_id}, " f"Name: {self.__name}, " 
                f"Specialty: {self.__specialty}")


    def validate_practitioner_details(self, practitioner_id, name, specialty):
        if not practitioner_id:
            raise ValueError("Invalid practitioner id")
        if not name:
            raise ValueError("Invalid name")
        if not specialty:
            raise ValueError("Invalid specialty")

    def set_practitioner_id(self, practitioner_id):
        if not practitioner_id:
            raise ValueError("Invalid practitioner id")
        self.__practitioner_id = practitioner_id

    def set_name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.__name = name

    def set_specialty(self, specialty):
        if not specialty:
            raise ValueError("Invalid specialty")
        self.__specialty = specialty

    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_name(self):
        return self.__name

    def get_specialty(self):
        return self.__specialty

    def add_availability(self, time_slot: datetime):
        if not isinstance(time_slot, datetime):
            raise TypeError("Invalid time slot")

        self.__availability.append(time_slot)

    def get_availability(self):
        return self.__availability

    def is_available(self, time_slot: datetime):
        return time_slot in self.__availability

    def book_slot(self, time_slot: datetime):
        if time_slot not in self.__availability:
            raise ValueError("Time slot is not available")
        self.__availability.remove(time_slot)