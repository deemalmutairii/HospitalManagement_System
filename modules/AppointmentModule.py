import pandas as pd
from repositories.AppointmentRepository import AppointmentRepository

class AppointmentModule:
    def __init__(self, db_helper):
        self.appointment_repo = AppointmentRepository(db_helper)

    def add(self, patient_id, doctor_id, date):
        try:
            self.appointment_repo.add_appointment(patient_id, doctor_id, date)
            print("Appointment added successfully.")
        except Exception as e:
            print(f"Failed to add appointment: {e}")

    def get_all_appointments(self):
        try:
            result = self.appointment_repo.get_all_appointments()
            return pd.DataFrame(result, columns=['appointment_id', 'patient_id', 'doctor_id', 'date'])
        except Exception as e:
            print(f"Failed to retrieve appointments: {e}")
            return pd.DataFrame()
