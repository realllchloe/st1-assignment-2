AI OFF -\> AI ON -\> VERIFY \| 1 hour

# Learning objectives

- Analyse the SmartCare client brief.

- Identify stakeholders and scope.

- Write functional and non-functional requirements.

- Develop user stories and Given-When-Then acceptance criteria.

- Use AI to critique requirements without allowing it to invent
  stakeholder needs.

- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate
bookings, difficulty finding patient information, inconsistent
appointment status and limited appointment history. Management wants a
small, maintainable patient, practitioner and appointment system.

# Part B - Stakeholders and Scope: AI OFF

Identify at least four stakeholders. Create In Scope and Out of Scope
lists. Label uncertain features as provisional rather than confirmed.

# Part C - Functional Requirements: AI OFF

Write 8-12 numbered functional requirements using FR-01, FR-02 and so
on. Each should describe one observable capability.

# Part D - Non-Functional Requirements: AI OFF

Write 4-6 numbered non-functional requirements covering appropriate
qualities such as reliability, maintainability, usability, data
integrity or testability.

# Part E - User Stories and Acceptance Criteria: AI OFF

Write 4-6 user stories. For at least three, create Given-When-Then
acceptance criteria including one negative or failure scenario.

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare
requirements for ambiguity, inconsistency, missing clarification
questions and testability. Do NOT invent new client requirements. For
every suggestion, state whether it is based on evidence or is only a
question/assumption requiring validation.

# Part G - VERIFY the AI Review

Classify each significant AI suggestion as Accepted, Modified, Rejected,
or Unverified. Explain the evidence used.

# Part H - Finalise SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user
stories, acceptance criteria, assumptions/open questions and selected AI
review evidence.

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent
or overreach on? Which requirement changed after review? Why must
requirements ve evidence?

AI noticed that there were some assumptions I made but did not mention
in the assumptions section, and AI also identified some details that I
missed. For example, for appointment status, AI identified that we need
to clarify what types of status the system should support. If we do not
know this, we cannot properly design this part of the system.

Due to the prompt, AI was not allowed to invent new client requirements.
When I asked AI to make some suggestions more specific, it reminded me
that it could not add details that were not provided by the client.
However, AI sometimes followed assumptions that I had made without
checking whether they were supported by the client requirements. For
example, it suggested which patient details should be searchable, but
the client only mentioned difficulty locating patient records and did
not require a search function.

Through the review, I also found that I had missed some information in
my original work. I changed the patient record question to first clarify
how patient records should be located. I also added more assumptions and
open questions that I had missed before.

Requirements need evidence because they need to match the client's
intent, rather than taking our own ideas for granted. Otherwise, we may
make assumptions in the same way as AI.
