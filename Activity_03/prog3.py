#3.3. Practical Problem Solving with String Manipulation and File Handling
lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
contactno = input("Enter contact number: ")
course = input("Enter course: ")

student_info = f"Last Name: {lname}\nFirst Name: {fname}\nAge: {age}\nContact Number: {contactno}\nCourse: {course}\n"

with open("Activity_03\students.txt", "w") as file:
    file.write(student_info)

print("\nStudent information has been saved to 'students.txt'.")
