from datetime import datetime
from patient import Patient
from practitioner import Practitioner
from appointment import Appointment


def main():
    print("---- Create Valid Objects ----")
    patient1 = Patient("001","Alice","0400123456")
    doctor1 = Practitioner("P001","Dr Smith","General Practice")
    time_slot1 = datetime(2026, 10, 1, 10, 0)
    doctor1.add_availability(time_slot1 )
    appointment1 = Appointment("A001", patient1, doctor1, datetime(2026, 10, 1, 10, 0))
    print(patient1)
    print(doctor1)
    print(appointment1)

    print("\n---- Test Invalid Input ----")
    try:
        patient2 = Patient("","Alice","")
    except ValueError as e:
        print(e)

    print("\n---- Test Cancellation ----")

    appointment1.cancel()
    print(appointment1.get_status())

    print("\n---- Test Invalid Status Transition ----")
    try:
        appointment1.cancel()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()