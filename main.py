import os
from dbmanger.PostgresHelper import PostgresHelper
from dbmanger.MongoHelper import MongoHelper
from modules.PatientModule import PatientModule


def main():
    """Main function to run the Hospital Management System."""
    db_type = os.getenv("DB_TYPE", "POSTGRES").lower()

    # Initialize the correct database helper
    if db_type == "postgres":
        db_helper = PostgresHelper(
            host="localhost",
            db_name="hospital_db",
            user="postgres",
            password="Deem1425"
        )
    elif db_type == "mongo":
        db_helper = MongoHelper(uri="mongodb://localhost:27017/", db_name="hospital")
    else:
        raise ValueError("Unsupported database type.")

    # Initialize PatientModule
    patient_module = PatientModule(db_helper, db_type)

    # Run operations
    while True:
        print("\nWelcome to the Hospital Management System!")
        print("1. Add Patient")
        print("2. Get All Patients")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            condition = input("Enter patient condition: ")
            patient_module.add(name, age, condition)
        elif choice == "2":
            patient_module.get_all()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
