class AppointmentRepository:

    def save(self, appointment):
        raise NotImplementedError

    def find_by_id(self, appointment_id):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def update(self, appointment):
        raise NotImplementedError