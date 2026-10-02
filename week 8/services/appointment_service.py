from domain.appointment import Appointment

class AppointmentService:
    def __init__(self, appointment_repository):
        self.appointment_repository = appointment_repository

    def create_appointment(self, appointment_id, patient, practitioner, appointment_datetime):
        if not practitioner.is_available(appointment_datetime):
            raise ValueError("Time slot is not available")

        appointment = Appointment(appointment_id, patient, practitioner, appointment_datetime)
        practitioner.book_slot(appointment_datetime)
        self.appointment_repository.save(appointment)
        return appointment

    def cancel_appointment(self, appointment_id):
        appointment = self.appointment_repository.find_by_id(appointment_id)

        if appointment is None:
            raise ValueError("Appointment not found")
        # Apply the appointment's domain behaviour
        appointment.cancel()
        # Coordinate the cancellation workflow
        practitioner = appointment.get_practitioner()
        appointment_datetime = appointment.get_appointment_datetime()
        practitioner.add_availability(appointment_datetime)

        self.appointment_repository.update(appointment)

        return appointment