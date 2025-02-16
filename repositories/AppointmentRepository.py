import pandas as pd
from dbmanger.PostgresHelper import PostgresHelper as PgHelper
from dbmanger.MongoHelper import MongoHelper as MgHelper

class AppointmentRepository:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def get_all_appointments(self):
        """Retrieve all appointments from the database."""
        try:
            if isinstance(self.db_helper, PgHelper):
                query = "SELECT appointment_id, patient_id, doctor_id, appointment_date, status FROM appointments"
                result = self.db_helper.fetch_query(query)
                return pd.DataFrame(result, columns=['appointment_id', 'patient_id', 'doctor_id', 'appointment_date', 'status'])
            elif isinstance(self.db_helper, MgHelper):
                result = list(self.db_helper.get("appointments"))
                return pd.DataFrame(result)
        except Exception as e:
            print(f"Failed to retrieve appointments: {e}")
            return pd.DataFrame()

    def add_appointment(self, patient_id, doctor_id, date):
        """Add a new appointment to the database."""
        try:
            if isinstance(self.db_helper, PgHelper):
                query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)"
                self.db_helper.execute_query(query, (patient_id, doctor_id, date))
            elif isinstance(self.db_helper, MgHelper):
                self.db_helper.insert("appointments", {"patient_id": patient_id, "doctor_id": doctor_id, "appointment_date": date})
        except Exception as e:
            print(f"Failed to add appointment: {e}")
