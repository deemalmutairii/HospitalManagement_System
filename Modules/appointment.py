from Repositories import appointment_repo


class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_date, status):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = status

    def schedule(self):
        """
        Schedules a new appointment using appointment_repo.
        """
        appointment_repo.add_appointment(self.patient_id, self.doctor_id, self.appointment_date, self.status)

    def update_status(self, appointment_id, new_status):
        """
        Updates the status of an appointment.
        """
        appointment_repo.update_appointment_status(appointment_id, new_status)

    @staticmethod
    def get_info(appointment_id):
        """
        Retrieves appointment information by ID.
        """
        return appointment_repo.get_appointment_info(appointment_id)

    @staticmethod
    def get_appointments_by_patient(patient_id):
        """
        Retrieves all appointments for a specific patient.
        """
        return appointment_repo.get_appointments_by_patient(patient_id)
