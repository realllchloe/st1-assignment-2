AI OFF -\> AI ON -\> COMPARE -\> VERIFY \| 1 hour

# A - Requirements Review

Highlight nouns, verbs and business rules in SmartCare v0.2.

Nouns:  
Patient, Practitioner, Appointment, Receptionist, Clinic Manager, System
Administrator, Patient Information, Personal Information, Patient
Record, Practitioner Information, Practitioner Availability, Appointment
Information, Booking Details, Appointment Status, Appointment History,
Appointment Time, Booking Conflict, Duplicate Booking, Operational
Report, Clinic Activities, Clinic Operations, Appointment Process,
Search Function, User Account, Authorization, Security Measure, Response
Time, System.

Verbs:  
Create, make, cancel, retain, view, check, manage, update, store,
search, locate, find, generate, review, monitor, schedule, display,
access, protect, maintain, support, record, include, use.

Business rules:  
Cancelled appointments are retained, and their status is updated to
cancelled when they are cancelled.

Practitioner availability affects available appointment times, and
practitioners may manage their own availability. (Assumption)

Receptionists may create, view and manage appointments and patient
information, including locating patient records. (Assumption)

Patient records may contain different types of patient information and
may be located using a search function. (Assumption)

Appointments may record specific appointment information, use defined
appointment statuses, and retain cancelled appointments in appointment
history. (Assumption)

Clinic managers may monitor clinic activities and the appointment
process and use operational reports containing required clinic
information. (Assumption)

A system administrator may manage user accounts and authorisation.
(Assumption)

The system may require security measures to protect patient and clinic
information. (Assumption)

The system may need to support long-term use, future changes and
acceptable response times for common activities. (Assumption)

# B - Candidate Classes

Record candidate concepts, supporting requirements, state and behaviour.

# C - CRC Cards

Create CRC cards for Patient, Practitioner and Appointment.

# D - UML Model

Draw classes, attributes, operations, associations and multiplicities.

# E - AI Design Review

Ask AI to suggest classes and relationships using only confirmed
requirements; require supporting requirement IDs.

# F - Compare and Decide

Record at least one accepted, modified and rejected AI suggestion.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th>AI suggestion</th>
<th>Comparison</th>
<th>Decision</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td>Patient Class. Responsibilities: store and manage patient
information; support retrieval of patient records. Collaborator:
Appointment. Relationship: one Patient may be associated with multiple
Appointments.</td>
<td>AI puts record retrieval in the Patient class, but my model does
not. My model leaves the search function to the design stage.</td>
<td>Modified</td>
<td>Record retrieval does not need to be a responsibility of the Patient
class because the search function will be considered with record storage
at the design stage.</td>
</tr>
<tr>
<td>Practitioner Class. Responsibilities: store and manage practitioner
information; maintain practitioner availability information.
Collaborator: Appointment. Relationship: one Practitioner may be
associated with multiple Appointments.</td>
<td>AI suggests practitioner information and availability. My model also
includes these and gives more details, such as name and specialty.</td>
<td>Accepted</td>
<td><p>The practitioner needs to maintain its name and specialty because
this information belongs to the practitioner. It also needs to manage
availability because appointments are arranged according to practitioner
availability.</p>
<p>And appointment is a collaborator because an appointment needs
practitioner information and availability.</p></td>
</tr>
<tr>
<td>Patient–Appointment Relationship. One Patient may be associated with
multiple Appointments because appointment management must be linked to
patient</td>
<td>AI suggests the relationship between Patient and Appointment, but
this was already included in the previous Patient class suggestion.</td>
<td>Rejected</td>
<td>This relationship was already included and considered in the
previous Patient class suggestion, so it does not add new information to
the model.</td>
</tr>
</tbody>
</table>

# G - Python Skeletons

Create simple Patient, Practitioner and Appointment class skeletons.

class Patient:

    def __init__(self, patient_id: str, name: str, contact_details):

        self.patient_id = patient_id

        self.name = name

        self.contact_details = contact_details

    def validate_patient_details(self):

        # Validate patient details

        pass

    def view_appointment_information(self):

        # View appointment information and status

        Pass

class Practitioner:

    def __init__(self, name: str, specialty: str, availability):

        self.name = name

        self.specialty = specialty

        self.availability = availability

    def manage_availability(self):

        # Update practitioner availability

        pass

    def view_availability(self):

        # View practitioner availability

        pass

class Appointment:

    def __init__(self, patient_id: str, practitioner_name: str, date, time, status):

        self.patient_id = patient_id

        self.practitioner_name = practitioner_name

        self.date = date

        self.time = time

        self.status = status  # scheduled, cancelled, or completed

    def create_appointment(self):

        # Create a new appointment with Scheduled status

        pass

    def update_status(self):

        # Update the appointment status

        pass

    def cancel_appointment(self):

        # Use update_status() to change status to Cancelled

        pass

    def check_booking_conflicts(self):

        # Check for another appointment at the same date and time

        pass

# H - Consistency Check

Check model-code consistency; do not implement full behavior yet.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th><strong>Class</strong></th>
<th><strong>Type</strong></th>
<th><strong>UML Model</strong></th>
<th><strong>Python Skeleton</strong></th>
<th><strong>Consistent?</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">Patient</td>
<td>Attribute</td>
<td>patient ID</td>
<td>patient_id</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>patient name</td>
<td>name</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>contact details</td>
<td>contact_details</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>validate patient details()</td>
<td>validate_patient_details()</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>view appointment information()</td>
<td>view_appointment_information()</td>
<td>Yes</td>
</tr>
<tr>
<td rowspan="7">Practitioner</td>
<td>Attribute</td>
<td>practitioner name</td>
<td>name</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>specialty</td>
<td>specialty</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>availability</td>
<td>availability</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>manage availability()</td>
<td>manage_availability()</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>view availability()</td>
<td>view_availability()</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>patient ID</td>
<td>patient_id</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>practitioner name</td>
<td>practitioner_name</td>
<td>Yes</td>
</tr>
<tr>
<td rowspan="7">Appointment</td>
<td>Attribute</td>
<td>date</td>
<td>date</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>time</td>
<td>time</td>
<td>Yes</td>
</tr>
<tr>
<td>Attribute</td>
<td>status</td>
<td>status</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>create appointment()</td>
<td>create_appointment()</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>update status()</td>
<td>update_status()</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>cancel appointment()</td>
<td>cancel_appointment()</td>
<td>Yes</td>
</tr>
<tr>
<td>Behaviour</td>
<td>check booking conflicts()</td>
<td>check_booking_conflicts()</td>
<td>Yes</td>
</tr>
</tbody>
</table>

# Reflection

What modelling decision was hardest? Where did AI over-design? What
evidence supported your final choices?

The hardest part was identifying classes and their CRC cards from the
requirements. This required carefully identifying nouns and verbs in the
requirements, then deciding which ones should become classes, attributes
or behaviors. A class should represent an independent concept with its
own attributes or behaviors. The identification process may result in
more classes than the system needs. Therefore, each possible class needs
to be checked to ensure it aligns with the system requirements to avoid
scope creep. It also required considering the business rules and
requirements to identify what each class needs to know and do. This is a
detailed analysis rather than simply choosing every noun or verb as part
of the model.

AI over-designed the model by suggesting many Manager and Controller
classes. Some suggestions also included design and implementation
details at the domain modelling stage. In addition, the AI also repeated
some suggestions.

My final choices were based on the client requirements and the
assumptions identified in Stage_2_SmartCare_v02. I checked that each
class, responsibility and relationship aligned with this evidence before
including it in the final model. The AI suggestions were reviewed and
adjusted according to the requirements and assumptions.
