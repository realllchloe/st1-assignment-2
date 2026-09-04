Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot)
Suggested prompt structure:
Act as a Python tutor.
I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

Microsoft copilot response:
1. What the Code Does

This program demonstrates a simple clinic appointment booking system in two stages.
Task 1 (Basic Version)
•	Displays a welcome message.
•	Stores appointment details in separate variables.
•	Prints two appointment records using f-strings.
Example:
Python
1
patient1_name = 'Alice Smith'
2
practitioner1_name = 'Dr. John Doe'
Show more lines
The information is stored manually and then displayed.
 
Task 1 Enhanced Version
The enhanced version improves the design by using:
•	List (appointments) to store multiple appointments.
•	Dictionary to store appointment details.
•	Functions to organize code into reusable blocks.
The book_appointment() function:
•	Accepts appointment details as parameters.
•	Checks that the patient name is not empty.
•	Creates a dictionary containing appointment information.
•	Adds the appointment to the appointments list.
The display_appointments() function:
•	Checks whether any appointments exist.
•	Displays all stored appointments.
This approach is more scalable than creating separate variables for every appointment.
 
2. Three Limitations

Limitation 1: No User Input
The appointment information is hard-coded into the program.
Issue: Users cannot enter their own appointment details while the program is running.
 
Limitation 2: Limited Validation
Only the patient name is validated.
Issue: The program allows empty practitioner names or invalid appointment times.
 
Limitation 3: Duplicate Bookings Are Possible
The system does not check whether a practitioner already has an appointment at the same time.
Issue: This could result in scheduling conflicts.
 
3. Suggested Improvements
Improvement 1
Add user input functionality to allow users to enter appointment details dynamically.
Improvement 2
Validate practitioner names and appointment times to improve data accuracy.
Improvement 3
Prevent double-booking by checking for existing appointments before storing a new one.
 

4. Overall Evaluation
The enhanced version is a good improvement because it introduces:
•	Functions
•	Lists
•	Dictionaries
•	Basic validation
These features make the program more organized, reusable, and easier to expand in future versions.
 

5. Questions to Test Your Understanding

Question 1
Why is using a list of dictionaries more flexible than creating variables such as:
Python
1
patient1_name
2
patient2_name
3
patient3_name
Show more lines
for every appointment?
My answer: It will be more easier to manage and display the data. We don not need to create a new variable for each new appointment.
 
Question 2
What would happen if the following code was executed?
Python
1
book_appointment("", "Dr. John Doe", "2024-07-20 10:00 AM")
Show more lines
Why does that happen?
My answer: Display “Patient name cannot be empty”.
 
Explanation Summary

This code demonstrates the progression from a simple hard-coded program to a more structured solution using functions, lists, and dictionaries. The main areas for improvement are user interaction, data validation, and booking conflict prevention. These enhancements would make the system more practical and reliable.

