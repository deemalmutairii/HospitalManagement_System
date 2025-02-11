from utils.DB_Helper import DBHelper


def add_appointment(patient_id, doctor_id, appointment_date, status):
    """
    Adds a new appointment to the database.
    """
    query = """
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
    VALUES (%s, %s, %s, %s)
    """
    db_helper = DBHelper()
    db_helper.set(query, (patient_id, doctor_id, appointment_date, status))


def update_appointment_status(appointment_id, new_status):
    """
    Updates the status of an appointment.
    """
    query = "UPDATE appointments SET status = %s WHERE appointment_id = %s"
    db_helper = DBHelper()
    db_helper.set(query, (new_status, appointment_id))


def get_appointment_info(appointment_id):
    """
    Retrieves appointment information by appointment ID.
    """
    query = "SELECT patient_id, doctor_id, appointment_date, status FROM appointments WHERE appointment_id = %s"
    db_helper = DBHelper()
    result = db_helper.get(query, (appointment_id,))
    return result[0] if result else None


def get_appointments_by_patient(patient_id):
    """
    Retrieves all appointments for a specific patient.
    """
    query = "SELECT appointment_id, doctor_id, appointment_date, status FROM appointments WHERE patient_id = %s"
    db_helper = DBHelper()
    result = db_helper.get(query, (patient_id,))
    return result
