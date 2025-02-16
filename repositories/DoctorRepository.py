import pandas as pd
from dbmanger.PostgresHelper import PostgresHelper as PgHelper
from dbmanger.MongoHelper import MongoHelper as MgHelper

class DoctorRepository:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def get_all_doctors(self):
        """Retrieve all doctors from the database."""
        try:
            if isinstance(self.db_helper, PgHelper):
                query = "SELECT doctor_id, name, phone, specialization FROM doctors"
                result = self.db_helper.fetch_query(query)
                return pd.DataFrame(result, columns=['doctor_id', 'name', 'phone', 'specialization'])
            elif isinstance(self.db_helper, MgHelper):
                result = list(self.db_helper.get("doctors"))
                return pd.DataFrame(result)
        except Exception as e:
            print(f"Failed to retrieve doctors: {e}")
            return pd.DataFrame()

    def add_doctor(self, name, phone, specialization):
        """Add a new doctor to the database."""
        try:
            if isinstance(self.db_helper, PgHelper):
                query = "INSERT INTO doctors (name, phone, specialization) VALUES (%s, %s, %s)"
                self.db_helper.execute_query(query, (name, phone, specialization))
            elif isinstance(self.db_helper, MgHelper):
                self.db_helper.insert("doctors", {"name": name, "phone": phone, "specialization": specialization})
        except Exception as e:
            print(f"Failed to add doctor: {e}")

    def update_doctor(self, doctor_id, name, phone, specialization):
        """Update an existing doctor's information."""
        try:
            if isinstance(self.db_helper, PgHelper):
                query = "UPDATE doctors SET name = %s, phone = %s, specialization = %s WHERE doctor_id = %s"
                self.db_helper.execute_query(query, (name, phone, specialization, doctor_id))
            elif isinstance(self.db_helper, MgHelper):
                query = {"_id": doctor_id}
                update_data = {"name": name, "phone": phone, "specialization": specialization}
                self.db_helper.update("doctors", query, update_data)
        except Exception as e:
            print(f"Failed to update doctor: {e}")
