import pandas as pd
from repositories.DoctorRepository import DoctorRepository

class DoctorModule:
    def __init__(self, db_helper):
        self.doctor_repo = DoctorRepository(db_helper)

    def add(self, name, specialty, phone):
        try:
            self.doctor_repo.add_doctor(name, specialty, phone)
            print("Doctor added successfully.")
        except Exception as e:
            print(f"Failed to add doctor: {e}")

    def update_info(self, doctor_id, name, specialty, phone):
        try:
            self.doctor_repo.update_doctor(doctor_id, name, specialty, phone)
            print("Doctor updated successfully.")
        except Exception as e:
            print(f"Failed to update doctor: {e}")

    def get_all_doctors(self):
        try:
            result = self.doctor_repo.get_all_doctors()
            return pd.DataFrame(result, columns=['doctor_id', 'name', 'specialty'])
        except Exception as e:
            print(f"Failed to retrieve doctors: {e}")
            return pd.DataFrame()
