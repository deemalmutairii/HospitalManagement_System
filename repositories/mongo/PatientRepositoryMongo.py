from dbmanger.MongoHelper import MongoHelper
import pandas as pd

class PatientRepositoryMongo:
    def __init__(self, db_helper: MongoHelper):
        self.db_helper = db_helper

    def get_all_patients(self):
        result = list(self.db_helper.get("patients"))
        return pd.DataFrame(result)

    def add_patient(self, name, age, condition):
        self.db_helper.insert("patients", {"name": name, "age": age, "condition": condition})
        print("Patient added successfully.")

    def update_patient(self, patient_id, name, age, condition):
        pass
