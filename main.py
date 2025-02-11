from Modules.patient import Patient
from Modules.doctor import Doctor
from Modules.appointment import Appointment

# Example: Adding a new patient
Patient("John Doe", "+1234567890", "123 Main St", 30).add()

# Example: Retrieve and print patient information
patient_id = Patient.get_id("+1234567890")
if patient_id:
    name, phone, address, age = Patient.get_info(patient_id)
    print(f"Patient Info: {name}, {phone}, {address}, {age}")

# Example: Adding a new doctor
Doctor("Dr. Alice Johnson", "+1123456789", "Cardiology").add()

# Example: Retrieve and print doctor information
doctor_id = 1  # Assuming doctor ID is known
doctor_info = Doctor.get_info(doctor_id)
if doctor_info:
    name, phone, specialization = doctor_info
    print(f"Doctor Info: {name}, {phone}, {specialization}")

# Example: Scheduling an appointment
Appointment(patient_id=1, doctor_id=1, appointment_date="2025-03-01 10:00:00", status="scheduled").schedule()

# Example: Retrieve and print appointment information
appointment_id = 1  # Assuming appointment ID is known
appointment_info = Appointment.get_info(appointment_id)
if appointment_info:
    patient_id, doctor_id, appointment_date, status = appointment_info
    print(f"Appointment Info: Patient ID: {patient_id}, Doctor ID: {doctor_id}, Date: {appointment_date}, Status: {status}")
