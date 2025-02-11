from Repositories import patient_repo

class Patient:
    def __init__(self, name, phone, address, age):
        self.name = name
        self.phone = phone
        self.address = address
        self.age = age

    def add(self):
        """
        Adds a new patient using patient_repo.
        """
        patient_repo.add_patient(self.name, self.phone, self.address, self.age)

    def update_info(self, patient_id):
        """
        Updates the patient information.
        """
        patient_repo.update_patient(patient_id, self.name, self.phone, self.address, self.age)

    @staticmethod
    def get_id(phone):
        """
        Retrieves patient ID by phone number.
        """
        return patient_repo.get_patient_id(phone)

    @staticmethod
    def get_info(patient_id):
        """
        Retrieves patient information by ID.
        """
        return patient_repo.get_patient_info(patient_id)
