from repositories.appointment_repository import AppointmentRepository

class InMemoryAppointmentRepository(AppointmentRepository):

    def __init__(self):
        self.items = {}

    def save(self, appointment):
        self.items[appointment.get_appointment_id()] = appointment

    def find_by_id(self, appointment_id):
        appointment = self.items.get(appointment_id)
# Removed based on AI review:
# AppointmentService already handles the appointment-not-found condition.
        #if appointment is None:
            #print("Appointment not found")

        return appointment

    def find_all(self):
        return list(self.items.values())

    def update(self, appointment):
        appointment_id = appointment.get_appointment_id()

        if appointment_id not in self.items:
            raise ValueError("Appointment not found")

        self.items[appointment_id] = appointment