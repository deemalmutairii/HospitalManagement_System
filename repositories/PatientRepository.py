from dbmanger.PostgresHelper import PostgresHelper as PgHelper
from dbmanger.MongoHelper import MongoHelper as MgHelper
import pandas as pd

class PatientRepository:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def get_all_patients(self):
        if isinstance(self.db_helper, PgHelper):
            query = "SELECT patient_id, name, age FROM patients"
            result = self.db_helper.fetch_query(query)
            return pd.DataFrame(result, columns=['patient_id', 'name', 'age'])
        elif isinstance(self.db_helper, MgHelper):
            result = list(self.db_helper.get("patients"))
            return pd.DataFrame(result)

    def add_patient(self, name, age):
        if isinstance(self.db_helper, PgHelper):
            query = "INSERT INTO patients (name, age) VALUES (%s, %s)"
            self.db_helper.execute_query(query, (name, age))
        elif isinstance(self.db_helper, MgHelper):
            self.db_helper.insert("patients", {"name": name, "age": age})

    def update_patient(self, patient_id, name, age, condition):
        if isinstance(self.db_helper, PgHelper):
            query = "UPDATE patients SET name = %s, age = %s, condition = %s WHERE patient_id = %s"
            self.db_helper.execute_query(query, (name, age, condition, patient_id))
        elif isinstance(self.db_helper, MgHelper):
            query = {"_id": patient_id}
            update_data = {"name": name, "age": age, "condition": condition}
            self.db_helper.update("patients", query, update_data)
