from dbmanger.PostgresHelper import PostgresHelper
import pandas as pd

class PatientRepositoryPostgres:
    def __init__(self, db_helper: PostgresHelper):
        self.db_helper = db_helper

    def get_all_patients(self):
        query = "SELECT patient_id, name, age, condition FROM patients"
        result = self.db_helper.fetch_query(query)
        return pd.DataFrame(result, columns=['patient_id', 'name', 'age', 'condition'])

    def add_patient(self, name, age, condition):
        query = "INSERT INTO patients (name, age, condition) VALUES (%s, %s, %s)"
        self.db_helper.execute_query(query, (name, age, condition))
        print("Patient added successfully.")
