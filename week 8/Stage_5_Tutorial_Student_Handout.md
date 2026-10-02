Week 8 \| 60 minutes

# Activity 1 - Where Does This Belong?

| Responsibility | Layer | Reason |
|----|----|----|
| Read menu input | PRESENTATION | The Presentation Layer is responsible for receiving user input and handling how the system communicates with the user. Reading menu input is included in user interaction. |
| Check appointment status transition | DOMAIN | Appointment status transitions are part of the business rules of the system. The Domain Layer includes business rules. |
| Coordinate booking use case | SERVICE | Booking an appointment involves several steps that need to be coordinated. The Service Layer is responsible for coordinating application use cases. |
| Execute SQLite INSERT | PERSISTENCE | Executing an SQLite INSERT is a database-storage operation. The Persistence Layer is responsible for implementing how data is actually stored. |
| Format confirmation message | PRESENTATION | Formatting a confirmation message determines how information is presented to the user. This responsibility belongs to the Presentation Layer. |
| Find appointment by ID | REPOSITORY | Finding an appointment by ID is a data-access operation. The Repository Layer provides an abstraction for retrieving data. |

# Activity 2 - Architecture Smell Hunt

**A SmartCare file contains input(), SQL, appointment conflict rules, printing and validation. Identify at least five architecture problems and propose a layer for each responsibility.**

The SmartCare file contains many different responsibilities in one file, which looks like a God Class. We need to separate these responsibilities based on the five architecture layers so that each layer has its own responsibility.

Input belongs to the Presentation Layer because it involves interaction with the user. SQL belongs to the Persistence Layer because it handles how data is stored. Appointment conflict rules belong to the Domain Layer because they are business rules. Printing belongs to the Presentation Layer because it involves formatting and presenting information to the user. Validation depends on what is being validated. If validation is part of coordinating the application process, it belongs to the Service Layer due to the coordination. If validation checks a business rule, it belongs to the Domain Layer.

# Activity 3 - SOLID Without Overengineering

**ClinicManager handles every use case. Which principle is threatened?**

The Single Responsibility Principle is threatened because ClinicManager handles many use cases. It should be separated into different classes.

**AppointmentService imports sqlite3 directly. What dependency concern exists?**

SQL belongs to the Persistence Layer, but now AppointmentService directly depends on sqlite3. Based on the Dependency Inversion Principle, it should depend on a repository abstraction, so the data storage method can be changed without changing the Service Layer.

**A repository interface has 20 methods but a client needs two. What concern exists?**

Based on the Interface Segregation Principle, the concern is that the client is forced to depend on methods it does not use.

**Should every class have an interface? Explain.**

No. Not every class needs an interface. An interface should be used when it is needed. Creating interfaces for every class can make the design unnecessarily complex.

# Activity 4 - AI Architecture Critique

**AI proposes microservices, an event bus, six interfaces and a dependency-injection framework. Decide what to reject, defer or keep using current requirements.**

Based on the current requirements, SmartCare is a small and manageable application. Microservices will be rejected because the current requirements do not need many independent services to be managed separately. The event bus will be deferred because it is not required by the current requirements, but it could be considered if the system becomes larger in the future. Six interfaces will be rejected because the current requirements do not need six interfaces and creating too many interfaces can make the design unnecessarily complex. The dependency-injection framework will be rejected because SmartCare is a small application, so simple dependency injection is enough for the current requirements.
