import os


file_path = "Activity_04/students.txt"


def load_records():
    records = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    student_id, fullname, class_standing, major_exam = parts
                    records.append((student_id, tuple(fullname.split()), float(class_standing), float(major_exam)))
    return records


def save_records(records, path=None):
    path = path or file_path
    with open(path, "w") as file:
        for record in records:
            file.write(f"{record[0]},{' '.join(record[1])},{record[2]},{record[3]}\n")


def calculate_grade(record):
    return (record[2] * 0.6) + (record[3] * 0.4)


def show_all_records(records):
    for record in records:
        print(record)

def order_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

def order_by_grade(records):
    return sorted(records, key=calculate_grade, reverse=True)

def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found.")

def add_record(records):
    student_id = input("Enter Student ID (6-digit): ")
    fullname = input("Enter Full Name: ").split()
    class_standing = float(input("Enter Class Standing: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, tuple(fullname), class_standing, major_exam))
    save_records(records)
    print("Record added successfully.")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            fullname = input("Enter New Full Name: ").split()
            class_standing = float(input("Enter New Class Standing: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            records[i] = (student_id, tuple(fullname), class_standing, major_exam)
            save_records(records)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    records = [record for record in records if record[0] != student_id]
    save_records(records)
    print("Record deleted successfully.")


def main():
    records = load_records()
    while True:
        print("\nMenu:")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            show_all_records(records)
        elif choice == "2":
            records = order_by_last_name(records)
            show_all_records(records)
        elif choice == "3":
            records = order_by_grade(records)
            show_all_records(records)
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            show_student_record(records, student_id)
        elif choice == "5":
            add_record(records)
        elif choice == "6":
            edit_record(records)
        elif choice == "7":
            delete_record(records)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
