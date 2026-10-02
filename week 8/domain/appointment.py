from datetime import datetime
from enum import Enum
from domain.patient import Patient
from domain.practitioner import Practitioner

class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, appointment_datetime: datetime):
        # Validate details before creating the appointment state
        self.validate_appointment_details(appointment_id, patient, practitioner, appointment_datetime)
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__appointment_datetime = appointment_datetime
        self.__status = AppointmentStatus.SCHEDULED

    def __str__(self):
        return (f"Appointment ID: {self.__appointment_id}, "f"Patient: {self.__patient.get_name()}, "f"Practitioner: {self.__practitioner.get_name()}, "
        f"Date/Time: {self.__appointment_datetime}, "f"Status: {self.__status.value}")

    def validate_appointment_details(self, appointment_id, patient, practitioner, appointment_datetime):
        if not appointment_id:
            raise ValueError("Invalid appointment id")

        if not isinstance(patient, Patient):
            raise TypeError("Invalid patient")

        if not isinstance(practitioner, Practitioner):
            raise TypeError("Invalid practitioner")

        if not isinstance(appointment_datetime, datetime):
            raise TypeError("Invalid appointment datetime")

    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient(self):
        return self.__patient

    def get_practitioner(self):
        return self.__practitioner

    def get_appointment_datetime(self):
        return self.__appointment_datetime

    def get_status(self):
        return self.__status

    def cancel(self):
        if self.__status == AppointmentStatus.COMPLETED:
            raise ValueError("Completed appointment cannot be cancelled")

        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment already cancelled")

        self.__status = AppointmentStatus.CANCELLED

    def complete(self):
        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointment cannot be completed")

        if self.__status == AppointmentStatus.COMPLETED:
            raise ValueError("Appointment already completed")

        self.__status = AppointmentStatus.COMPLETED