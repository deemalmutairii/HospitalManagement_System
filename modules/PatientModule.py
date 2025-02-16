from repositories.postgres.PatientRepositoryPostgres import PatientRepositoryPostgres
from repositories.mongo.PatientRepositoryMongo import PatientRepositoryMongo
from utils.InformationMessages import PATIENT_ADDED_SUCCESS, PATIENT_UPDATED_SUCCESS

class PatientModule:
    def __init__(self, db_helper, db_type="postgres"):
        if db_type.lower() == "postgres":
            self.patient_repo = PatientRepositoryPostgres(db_helper)
        elif db_type.lower() == "mongo":
            self.patient_repo = PatientRepositoryMongo(db_helper)
        else:
            raise ValueError("Unsupported database type.")

    def add(self, name, age, condition):
        """Add a new patient."""
        self.patient_repo.add_patient(name, age, condition)
        print(PATIENT_ADDED_SUCCESS)

    def update_info(self, patient_id, name, age, condition):
        """Update patient information."""
        self.patient_repo.update_patient(patient_id, name, age, condition)
        print(PATIENT_UPDATED_SUCCESS)
