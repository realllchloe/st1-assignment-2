# 1. Problem and Scope

Problem:  
Using spreadsheets and paper records leads to duplicate bookings,
difficulty finding patient information, inconsistent appointment status
and limited appointment history.  
Scope:  
A small, maintainable system that can manage patients, practitioners and
appointments.

# 2. Stakeholders

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 29%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th>Stakeholder</th>
<th>Need</th>
<th>Evidence</th>
<th>Scope</th>
</tr>
</thead>
<tbody>
<tr>
<td>Practitioners</td>
<td>Check the appointments, review patient information and manage the
medical records.</td>
<td>The client mentioned that the system should support patient,
practitioner and appointment management.</td>
<td>In scope<br />
Provisional: These specific responsibilities are inferred from general
clinic operations and are not explicitly defined in the client
requirements.</td>
</tr>
<tr>
<td>Patient</td>
<td>Make appointments, check booking details and update the personal
information</td>
<td>The client mentioned that the system should support patient and
appointment management and identified inconsistent appointment status
information.</td>
<td>In scope<br />
Provisional: direct patient access and actions are not defined.</td>
</tr>
<tr>
<td>System admin</td>
<td>Manage the user accounts and authorization, maintain the
system.</td>
<td>The client does not explicitly mention system administration, user
accounts or authorization.</td>
<td><p>Not yet in scope:</p>
<p>System administration, user accounts and authorization are not
specified in the client requirements and require confirmation before
being included in scope.</p></td>
</tr>
<tr>
<td>Clinic manager</td>
<td>Monitor clinic activities and the appointment process</td>
<td>The client identified difficulty producing basic operational
reports.</td>
<td>In scope<br />
Provisional: These functions are inferred from general clinic system
operations, and the specific responsibilities are not defined in the
client requirements.</td>
</tr>
<tr>
<td>Receptionist</td>
<td>Create, view, and manage appointments and patient information.</td>
<td>The client mentioned patient and appointment management and
identified a lack of reliable appointment history.</td>
<td>In scope<br />
Provisional: Receptionists are not explicitly mentioned, and their
specific responsibilities are not defined.</td>
</tr>
</tbody>
</table>

# 3. Functional Requirements

FR-01: The system shall allow staff or patient to create an appointment.

FR-02: The system shall allow staff or patient to cancel an appointment

FR-03: The system shall retain cancelled appointments

FR-04: The system shall allow staff to view and manage practitioner
availability.

FR-05: The system shall allow staff to create and store patient records.

FR-06: The system shall allow staff to update appointment status.

FR-07: The system shall allow staff to update patient records.

FR-08: The system shall generate basic operational reports.

FR-09: The system shall check for booking conflicts.

FR-10: The system shall allow staff to search for patient records.

# 4. Non-Functional Requirements

NFR-01: Core system functions should be independently testable.

NFR-02: The system should be maintainable for long-term use.

NFR-03: The system should remain secure against common security
vulnerabilities.

NFR-04: should be updatable to reduce or increase the function.

NFR-05: The system should be easy for users to learn and use
independently.

NFR-06: The system should remain responsive when handling patient and
appointment data.

# 5. User Stories

US-01: As a clinic manager, I want to generate basic operational
reports, so that I can review clinic operations.

US-02: As a practitioner, I want to view and manage my availability, so
that appointments can be scheduled based on my available time.

US-03: As a receptionist, I want to search for patient records, so that
I can locate patient information quickly.

US-04: As a patient, I want to cancel an appointment, so that I can
manage my appointment when I am unavailable.

# 6. Acceptance Criteria

GIVEN the patient does not have an existing record in the system,  
WHEN the receptionist searches for the patient by name or other
information,  
THEN the system displays that no patient record was found.

GIVEN the patient has an existing appointment,  
WHEN the patient cancels the appointment,  
THEN the system updates the appointment status to cancelled.

GIVEN the practitioner needs to take leave,  
WHEN the practitioner updates their availability,  
THEN the system updates the available appointment times.

# 7. Assumptions and Open Questions

Assumption 1: Practitioners may check appointments, review patient
information, manage medical records and manage their own availability.  
Open Question: What information and functions should practitioners be
able to access and manage, including whether they should manage their
own availability?

Assumption 2: Patients may directly access the system to make
appointments, check booking details and update their personal
information.  
Open Question: Can patients directly access the system? If so, what
functions should they be able to perform?

Assumption 3: A system administrator may be required to manage user
accounts and authorisation and maintain the system.  
Open Question: Does the system require a system administrator to manage
user accounts and authorisation?

Assumption 4: Clinic managers may directly use the system to monitor
clinic activities and the appointment process.  
Open Question: What functions should clinic managers be able to access
and manage?

Assumption 5: Receptionists may be system users who create, view and
manage appointments and patient information, including searching for
patient records.  
Open Question: Will receptionists use the system, and what functions
should they be able to perform?

Assumption 6: Patient records may be searched using the patient's name
or other identifying information.  
Open Question: What information should be used to search for patient
records?

# 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
|----|----|----|----|----|
| Add an open question such as: "What appointment statuses should the system support?" Also clarify what each status means and when it should be used, so appointment status information remains consistent across the clinic. | The client specifically identified inconsistent appointment status information as a current problem, but the required statuses are not specified. | Accepted | The client mentioned inconsistent appointment status information but did not explain what statuses are needed. This detail is needed to understand how the appointment function should work. | Compared the suggestion with the requirements and confirmed that the appointment status details are missing and need clarification. |
| Add an open question such as: "What operational reports are required, who will use them, how frequently are they needed, and what information should they contain?" This clarifies the reporting requirement without assuming any report types. rather than creating new report types. | The client identified difficulty producing basic operational reports. No further report details are provided. | Accepted | This is a gap that I did not notice before. We need to know what reports are required and what information they should contain so that the reporting function can match the client’s requirements. | Compared the suggestion with the requirements and my open questions to confirm that the report details were not covered. |
| Expand Open Question 6 to ask: "Which patient details should be searchable?" This ensures the search function can effectively address the client’s record retrieval problem. | The client reported difficulty locating patient but did not specify how patient records should be located. | Modified | The client only said that it is difficult to locate patient records. This does not mean that a search function is required. Records may be located in another way. I also found that my original Open Question 6 made the same assumption. We need to confirm how patient records should be located first. | Compared “searchable” in the AI suggestion with “locating patient records” in the requirements and found that search was an assumption. I also checked my Open Question 6 and found the same problem. |
| Add an open question such as: "What information should be included in a patient record, and which fields are mandatory or optional?" This helps ensure patient records are managed consistently without assuming specific data fields. | Patient management is required, but the client has not specified the information to be included in patient records. | Accepted | This is a gap that I did not notice before. We need to know what information is required in a patient record before we can design and implement this requirement. | Compared the suggestion with the requirements and my open questions. The patient record details were not covered. |
| Add an open question such as: "What information should be recorded for each appointment?" Clarify what information is required to support appointment history, appointment cancellation and booking conflict checking. | The client requires appointment management and mentioned duplicate bookings, manual cancellations and lack of reliable appointment history, but did not say what information should be recorded for each appointment. | Modified | This is a gap that I did not notice before. We need to know what information should be recorded for each appointment. However, we also need to confirm whether cancelled appointments should be included in the appointment history. | Compared the suggestion with the requirements. Appointment details were missing, but the client did not specify whether cancelled appointments should be included in the appointment history. |
| Clarify with the client what “long-term use” means and what future changes are expected. For example, determine whether the clinic expects regular feature updates, workflow changes or system enhancements. This would provide a basis for assessing maintainability. | The client brief does not mention long-term use or maintainability. Long-term use came from my own assumption about the system. | Modified | I assumed that the system should support long-term use, but this was not stated by the client. I also found that I did not include this in my assumptions. We need to confirm whether maintainability is required first before asking about future changes. | Compared the suggestion with the requirements and my NFRs. Maintainability came from my own assumption. I also found that it was missing from my assumptions. |
| Clarify what security concerns exist for the clinic. For example, confirm whether patient information should only be accessible to authorized users, whether login mechanisms are required, and whether different user roles should have different access permissions. | The client brief does not provide any specific security requirements. | Modified | I included security as an NFR based on my own assumption, but the client did not state any security requirements. I also did not include this in my assumptions. We need to first confirm whether the client has any security requirements before asking for more specific details. | Compared the suggestion with the requirements and my NFRs. Security came from my own assumption. I also found that it was missing from my assumptions. |
| Clarify who the expected users are and what level of training they may require. For example, determine whether new users should be able to perform common tasks without assistance after a short introduction. | Client does not clearly define all expected system users or any user training requirements. | Modified | The client did not mention user training, so we should not assume that training is required. My existing questions only ask about the stakeholders I have already identified, but I did not ask whether there are other system users that I have missed. | Compared the suggestion with the requirements. User training was not mentioned. I also checked my stakeholder questions and found that I had not asked whether there are other system users. |
| Clarify which system activities require fast response times, such as searching for patient records, creating appointments or updating appointment information. Establish what level of delay would be considered unacceptable by users. | No specific performance or response-time expectations are provided in the client brief. | Modified | The client did not provide any specific performance or response-time requirements. I included performance as an NFR based on my own assumption, but I did not include this in my assumptions. We should first confirm whether the client has any performance expectations. If so, we can then ask which system activities need response-time requirements and what response time would be acceptable. | Compared the suggestion with the requirements and my performance NFR. Performance came from my own assumption, and I also found that it was missing from my assumptions. |

Modified Assumptions and Open Questions

Assumption 1: Practitioners may check appointments, review patient
information, manage medical records and manage their own availability.  
Open Question: What information and functions should practitioners be
able to access and manage, including whether they should manage their
own availability?

Assumption 2: Patients may directly access the system to make
appointments, check booking details and update their personal
information.  
Open Question: Can patients directly access the system? If so, what
functions should they be able to perform?

Assumption 3: A system administrator may be required to manage user
accounts and authorisation and maintain the system.  
Open Question: Does the system require a system administrator to manage
user accounts and authorisation?

Assumption 4: Clinic managers may directly use the system to monitor
clinic activities and the appointment process.  
Open Question: What functions should clinic managers be able to access
and manage?

Assumption 5: Receptionists may be system users who create, view and
manage appointments and patient information, including searching for
patient records.  
Open Question: Will receptionists use the system, and what functions
should they be able to perform?

Assumption 6: Patient records may be located using a search function.  
Open Question: How should patient records be located in the system? If a
search function is required, what information should be used to search
for patient records?

Assumption 7: Patient records may include different types of patient
information required by the clinic.  
Open Question: What information should be included in a patient record,
and which information is mandatory or optional?

Assumption 8: Each appointment may need to record specific appointment
information.  
Open Question: What information should be recorded for each appointment?

Assumption 9: Cancelled appointments may be included in the appointment
history.  
Open Question: Should cancelled appointments be included in the
appointment history?

Assumption 10: The system may need to support long-term use and future
changes.  
Open Question: Does the clinic have any maintainability requirements? If
so, what future changes or updates are expected?

Assumption 11: The system may need security measures to protect patient
and clinic information.  
Open Question: Does the clinic have any specific security requirements?
If so, what information needs to be protected and who should be allowed
to access it?

Assumption 12: There may be other system users in addition to the
stakeholders already identified.  
Open Question: Are there any other users who will directly use the
system? If so, what functions should they be able to perform?

Assumption 13: The system may need acceptable response times for common
system activities.  
Open Question: Does the clinic have any performance or response-time
expectations? If so, which system activities require response-time
requirements, and what response time would be acceptable?

Assumption 14: Operational reports may require specific information and
may be used by different clinic users.  
Open Question: What operational reports are required, who will use them,
how frequently are they needed, and what information should they
contain?

Assumption 15: The system may need a defined set of appointment
statuses.  
Open Question: What appointment statuses should the system support? What
does each status mean and when should it be used?
