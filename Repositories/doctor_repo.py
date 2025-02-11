from utils.DB_Helper import DBHelper


def add_doctor(name, phone, specialization):
    query = "INSERT INTO doctors (name, phone, specialization) VALUES (%s, %s, %s)"
    db_helper = DBHelper()
    db_helper.set(query, (name, phone, specialization))


def get_doctor_info(doctor_id):
    query = "SELECT name, phone, specialization FROM doctors WHERE doctor_id = %s"
    db_helper = DBHelper()
    result = db_helper.get(query, (doctor_id,))
    return result[0] if result else None
