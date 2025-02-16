import pandas as pd
from repositories.PatientRepository import PatientRepository

class PatientModule:
    def __init__(self, db_helper):
        self.patient_repo = PatientRepository(db_helper)

    def add(self, name, age, condition):
        try:
            self.patient_repo.add_patient(name, age, condition)
            print("Patient added successfully.")
        except Exception as e:
            print(f"Failed to add patient: {e}")

    def update_info(self, patient_id, name, age, condition):
        try:
            self.patient_repo.update_patient(patient_id, name, age, condition)
            print("Patient updated successfully.")
        except Exception as e:
            print(f"Failed to update patient: {e}")

    def get_all_patients(self):
        try:
            result = self.patient_repo.get_all_patients()
            return pd.DataFrame(result, columns=['patient_id', 'name', 'age', 'condition'])
        except Exception as e:
            print(f"Failed to retrieve patients: {e}")
            return pd.DataFrame()
