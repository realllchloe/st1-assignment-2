DESIGN FIRST -\> AI PAIR PROGRAMMING -\> REVIEW -\> VERIFY \| 1hour

# A - Revisit Approved UML

Confirm responsibilities, attributes and relationships before coding.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Class</th>
<th>Attributes</th>
<th>Responsibilities</th>
<th>Relationships</th>
</tr>
</thead>
<tbody>
<tr>
<td>Patient</td>
<td><p>patient ID,</p>
<p>name,</p>
<p>contact details</p></td>
<td>Maintain patient information and validate patient details to keep
the information valid.</td>
<td>Patient is related to Appointment because a patient can have
appointments.</td>
</tr>
<tr>
<td>Practitioner</td>
<td><p>practitioner ID,</p>
<p>name,</p>
<p>specialty,</p>
<p>availability</p></td>
<td>Maintain practitioner information and manage availability for
arranging appointments.</td>
<td>Practitioner is related to Appointment because a practitioner can
have appointments according to their availability.</td>
</tr>
<tr>
<td>Appointment</td>
<td>appointment ID, Patient, Practitioner, date/time, status</td>
<td>Maintain appointment information; handle booking, cancellation and
status changes; check practitioner availability to avoid booking
conflicts.</td>
<td>Appointment is related to Patient and Practitioner because an
appointment connects a patient with a practitioner.</td>
</tr>
</tbody>
</table>

# B - Implement Patient: AI OFF

**Implement Patient with type hints and basic validation.**

The code has been uploaded separately.

# C - Implement Practitioner: AI OFF

**Implement Practitioner with identifier, name and specialty; no
database logic.**

The code has been uploaded separately.

# D - Implement Appointment: AI ON

**Give AI the approved Appointment UML, business rules and explicit
constraints. Ask it to implement only Appointment and agreed
enum/exception.**

The code has been uploaded separately.

# E - Review Generated Code

**Check model consistency, unsupported features, public state mutation,
unnecessary inheritance, invented dependencies and error handling.**

The error handling was not consistent. The Appointment class used raise
for error handling. Then, I changed the error handling in Patient and
Practitioner to use raise to make it consistent. There are no
unsupported features, public state mutations, unnecessary inheritance or
invented dependencies.

# F - Manual Behaviour Checks

**Create valid objects, test invalid input, cancel a scheduled
appointment and attempt an illegal repeated transition.**

The code has been uploaded separately.

# G - Refactor

**Remove unnecessary code and make implementation simpler and
design-consistent.**

The error handling was not consistent. The Appointment class used raise
for error handling. Then, I changed the error handling in Patient and
Practitioner to use raise to make design consistent.

# H - AI Engineering Log

**Record prompt, generated contribution, decisions and verification
evidence.**

| Record prompt | generated contribution | decisions | verification evidence |
|----|----|----|----|
| Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML. | Generated the Appointment class from the approved SmartCare UML with associations to Patient and Practitioner, type hints, and the AppointmentStatus enum. | Accepted the generated Appointment class after modifying it to make it consistent with my Patient and Practitioner classes. I also added practitioner availability to prevent double booking. I checked the final version to ensure it met the assignment requirements before adopting it. | Created valid Patient, Practitioner and Appointment objects and confirmed the associations worked correctly. |
| After your explanation about returning error messages and using raise statements, I decided to use raise. Please show me how to apply it in the Appointment class. | Suggested using raise statements for validation and error handling. | After discussing different error handling approaches with AI, I accepted the AI suggestion and used raise statements in the Appointment class. | Tested invalid Patient input and confirmed validation errors were raised. |
| I need to add input validation to the Appointment class. What validation checks should I add and why? | Suggested adding input validation for appointment data using empty-value checks and isinstance() checks. | After discussing input validation with AI, I accepted the AI suggestion and added validation checks to the constructor. | Reviewed the suggested validation checks and applied them. |
| Explain how appointment status transitions should work. | Suggested using cancel() and complete() | After discussing appointment status transitions with AI, I accepted the AI suggestion and used cancel() and complete() methods to manage status changes. | Cancelled a scheduled appointment and attempted to cancel it again to test invalid status transitions. |

# Suggested AI prompt

Act as a Python pair programmer. Implement only the Appointment class
from the approved SmartCare UML. Use type hints and an AppointmentStatus
enum. Cancelled appointments remain as objects. Do not add database, UI,
notification or service classes. Protect status transitions and explain
any decision not directly visible in the UML.

# Reflection

Which AI-generated part did you modify or reject? Why? How did the
approved design constrain the AI?

I modified the Appointment class generated by AI using my Patient and
Practitioner classes. The original Appointment class used object for
Patient and Practitioner, so I changed it to use my Patient and
Practitioner classes to make the three classes work together. I also
found that the original version did not check Practitioner availability
when creating an appointment, so I added availability and booking checks
to prevent booking an unavailable time slot and double booking. I
changed the attributes to use double underscores to make the classes
consistent and protect the attributes. I accepted raise for error
handling and used it in Patient and Practitioner to make the error
handling consistent. I did not use @property because I preferred to use
the getter and setter methods that I learned in class. The approved UML
defined the classes, attributes, responsibilities and relationships for
SmartCare. In my prompt, I asked AI to follow this approved UML and not
add database, UI, notification or service classes. Therefore, the UML
and the prompt constrained the AI to follow the approved design.
