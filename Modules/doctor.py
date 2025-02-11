from Repositories import doctor_repo


class Doctor:
    def __init__(self, name, phone, specialization):
        self.name = name
        self.phone = phone
        self.specialization = specialization

    def add(self):
        """
        Adds a new doctor using doctor_repo.
        """
        doctor_repo.add_doctor(self.name, self.phone, self.specialization)

    @staticmethod
    def get_info(doctor_id):
        """
        Retrieves doctor information by ID.
        """
        return doctor_repo.get_doctor_info(doctor_id)
