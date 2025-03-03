#3.4 Activity for Reading File Contents and Display
file_path = "Activity_03/students.txt"

try:
    with open(file_path, "r") as file:
        print("\nReading Student Information:")
        print(file.read())
except FileNotFoundError:
    print("Error: 'students.txt' not found. Please ensure the file exists.")
