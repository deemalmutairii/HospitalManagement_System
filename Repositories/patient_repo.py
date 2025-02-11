from utils.DB_Helper import DBHelper


def add_patient(name, phone, address, age):
    query = "INSERT INTO patients (name, phone, address, age) VALUES (%s, %s, %s, %s)"
    db_helper = DBHelper()
    db_helper.set(query, (name, phone, address, age))


def update_patient(patient_id, name, phone, address, age):
    query = "UPDATE patients SET name = %s, phone = %s, address = %s, age = %s WHERE patient_id = %s"
    db_helper = DBHelper()
    db_helper.set(query, (name, phone, address, age, patient_id))


def get_patient_id(phone):
    query = "SELECT patient_id FROM patients WHERE phone = %s"
    db_helper = DBHelper()
    result = db_helper.get(query, (phone,))
    return result[0][0] if result else None


def get_patient_info(patient_id):
    query = "SELECT name, phone, address, age FROM patients WHERE patient_id = %s"
    db_helper = DBHelper()
    result = db_helper.get(query, (patient_id,))
    return result[0] if result else None
