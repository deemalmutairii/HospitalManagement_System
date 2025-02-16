import os
from dbmanger.PostgresHelper import PostgresHelper
from dbmanger.MongoHelper import MongoHelper
from modules.PatientModule import PatientModule
from modules.DoctorModule import DoctorModule
from modules.AppointmentModule import AppointmentModule


def display_main_menu():
    print("\nWelcome to the Hospital Management System!")
    print("1. Patient Operations")
    print("2. Doctor Operations")
    print("3. Appointment Operations")
    print("4. Exit")


def main():
    try:
        db_type = os.getenv("DB_TYPE", "POSTGRES")
        if db_type == 'POSTGRES':
            db_helper = PostgresHelper(
                host=os.getenv('POSTGRES_HOST', 'localhost'),
                db_name=os.getenv('POSTGRES_DB', 'hospital_db'),
                user=os.getenv('POSTGRES_USER', 'postgres_user'),
                password=os.getenv('POSTGRES_PASSWORD', 'securepassword'),
                port=int(os.getenv('POSTGRES_PORT', 5432))
            )
        elif db_type == 'MONGO':
            db_helper = MongoHelper(
                uri=os.getenv('MONGO_URI', "mongodb://localhost:27017/"),
                db_name=os.getenv('MONGO_DB_NAME', "hospital")
            )
        else:
            raise ValueError("Unsupported DB Type")

        patient_module = PatientModule(db_helper)
        doctor_module = DoctorModule(db_helper)
        appointment_module = AppointmentModule(db_helper)

        while True:
            display_main_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                handle_patient_operations(patient_module)
            elif choice == "2":
                handle_doctor_operations(doctor_module)
            elif choice == "3":
                handle_appointment_operations(appointment_module)
            elif choice == "4":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
