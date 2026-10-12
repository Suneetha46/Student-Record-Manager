
import re
import json

FILE_NAME = "students.txt"


# Validate Email using Regex
def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email) is not None


# Add Student
def add_student():
    try:
        name = input("Enter Student Name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty!")

        age = int(input("Enter Student Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than zero!")

        email = input("Enter Student Email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email address!")

        student = {
            "name": name,
            "age": age,
            "email": email
        }

        # Save Data to File
        with open(FILE_NAME, "a") as file:
            file.write(json.dumps(student) + "\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Invalid Input:", e)

    except OSError as e:
        print("File Error:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")

        for line in students:
            student = json.loads(line)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Email:", student["email"])
            print("----------------------")

    except FileNotFoundError:
        print("No student data file found. Add a student first.")

    except (OSError, json.JSONDecodeError) as e:
        print("Error reading student data:", e)


# Main Menu
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
