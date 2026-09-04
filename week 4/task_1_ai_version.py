# No Database
# No GUI

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):

    if patient_name == "":
        print("Patient name cannot be empty.")
        return

    if practitioner_name == "":
        print("Practitioner name cannot be empty.")
        return

    if appointment_time == "":
        print("Appointment time cannot be empty.")
        return

    # Prevent double-booking
    for appointment in appointments:
        if (
            appointment["practitioner"] == practitioner_name
            and appointment["time"] == appointment_time
        ):
            print("This appointment slot is already booked.")
            return

    # Create appointment record
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment booked successfully.")

def display_appointments():

    if not appointments:
        print("No appointments recorded.")
        return

    print("\nAppointment List")
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )

# Test data
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

# Duplicate booking test
book_appointment("Charlie Brown", "Dr. John Doe", "2024-07-20 10:00 AM")

display_appointments()