Week 7 \| 60 minutes

# Activity 1 - Encapsulation Review

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 50%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Class</th>
<th>Protected state / invariant</th>
<th>Public operations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Patient</td>
<td><p>State: patient_id, name, contact_details</p>
<p>Invariant: Keep patient details valid.</p></td>
<td><p>validate_patient_details(),</p>
<p>get/set patient details</p></td>
</tr>
<tr>
<td>Practitioner</td>
<td>State: practitioner_id, name, specialty, availability Invariant:
Keep availability valid.</td>
<td><p>get/set practitioner information, add_availability(),
get_availability(),</p>
<p>is_available(),</p>
<p>book_slot()</p></td>
</tr>
<tr>
<td>Appointment</td>
<td><p>State: appointment_id, Patient, Practitioner,
appointment_datetime, status</p>
<p>Invariant: Keep status as SCHEDULED, CANCELLED, or COMPLETED and
follow legal status transitions.</p></td>
<td><p>cancel(),</p>
<p>complete(),</p>
<p>get appointment information</p></td>
</tr>
</tbody>
</table>

# Activity 2 - Composition or Inheritance?

**Appointment and Patient -\> ☑ Composition/association □ Inheritance
Reason:**

An Appointment references a Patient. So, it is not a type of Patient.

**Appointment and Practitioner -\> ☑Composition/association □
Inheritance Reason:**

An Appointment references a Practitioner. So, it is not a type of
Practitioner.

**Doctor and Practitioner (hypothetical) -\> □ Composition/association
☑Inheritance Reason:**

Doctor is a type of Practitioner.

**Clinic and Appointment -\> ☑ Composition/association □ Inheritance
Reason:**

Clinic has Appointments. So, it is not a type of Appointment.

# Activity 3 - Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**

Appointment class

**Who validates a patient name?**

Patient class

**Should Appointment execute SQL? Why?**

No, because database operations are not the responsibility of
Appointment.

**Should the UI decide whether a status transition is legal?**

No, Appointment should decide whether its status transition is valid,
not the UI.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL
inside cancel(), a NotificationManager dependency and inheritance from
PatientRecord. Identify at least five design problems and corrections.

The Appointment class cannot have public status mutation. The status should only be changed by the methods in the Appointment class. The cancel() method should not have SQL because database operations are not the responsibility of Appointment. NotificationManager should not be added because it is not in the current requirements. Appointment should not inherit from PatientRecord because Appointment is not a type of PatientRecord, and PatientRecord should also not be added because it is not in the current requirements.

# Exit question

Why can code be object-oriented syntactically but still have poor
object-oriented design?

Code can include classes, attributes and methods, so it can be
object-oriented syntactically. But if the state and behaviours do not
belong to the correct class based on its responsibility, or the class
does not protect its invariants, it can still have poor object-oriented
design. Good object-oriented design should keep related state and
behaviour together and give each class a clear responsibility.
