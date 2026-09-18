Week 6 \| 60 minutes

# Candidate Concepts

| Candidate | Class? | Reason |
|----|----|----|
| Patient | Yes | Patient has common attributes based on the patient information stored in the system. |
| Practitioner | Yes | Practitioner has common attributes, such as availability. |
| Appointment | Yes | Appointment has attributes such as status, and it also has behaviors such as booking and cancellation. |
| Name | No | Name is an attribute of Patient or Practitioner. |
| Clinic | No | Clinic is the organization using the system, not a class in the domain model. |
| Database | No | Database has attributes and behaviors, but it is more about the technical field, not the SmartCare domain. |
| Cancellation | No | Cancellation is a behavior of Appointment. |
| Status | No | Status is attributes. |

# CRC Cards

## Patient

| Responsibilities | Collaborators |
|----|----|
| Maintain patient identity and basic information, including patient ID, name and contact details |  |
| Validate patient details and view appointment information and status | Appointment |

## Practitioner

| Responsibilities | Collaborators |
|----|----|
| Maintain practitioner information, including name and specialty |  |
| Provide and manage availability for appointments | Appointment |

## Appointment

| Responsibilities | Collaborators |
|----|----|
| Maintain appointment details, including the patient, practitioner, date, time and status | Patient, Practitioner |
| Process booking, cancellation, status changes and check booking conflicts. | Patient, Practitioner |

# Relationship Reasoning

**Patient to Appointment: which relationship and why?**

Association. Because Patient and Appointment are related, and they can
exist independently.

**Practitioner to Appointment: what multiplicity?**

Practitioner 1 ↔ 0..\* Appointment. A practitioner can have zero or many
appointments, and each appointment has exactly one practitioner.

**Should Appointment inherit from Patient?**

No. An Appointment is not a type of Patient, so inheritance is not
suitable.

**Does Clinic need to own every object?**

No. Clinic does not need to own every object because this may make
Clinic a God Class with too many responsibilities.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager,
AppointmentManager, ClinicController, NotificationManager,
ScheduleEngine.

| Ai suggestion | Decision | reason |
|----|----|----|
| PatientManager | Reject | The Patient class can be used directly instead of adding a separate PatientManager class. An additional class would make the model unnecessarily complex. |
| PractitionerManager | Reject | The Practitioner class can be used directly instead of adding a separate PractitionerManager class. An additional class would make the model unnecessarily complex. |
| AppointmentManager | Reject | The Appointment class can be used directly instead of adding a separate AppointmentManager class. An additional class would make the model unnecessarily complex. |
| ClinicController | Reject | ClinicController is related to system design and implementation. It is not needed at the domain modelling stage. |
| NotificationManager | Reject | The client did not mention a notification function. NotificationManager is not needed. |
| ScheduleEngine | Reject | ScheduleEngine is related to system design and implementation, so it is not needed at the domain modelling stage. |
