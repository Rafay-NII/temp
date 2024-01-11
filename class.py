import uuid
from datetime import datetime

class User:
    def __init__(self, userID, username, password):
        self.userID = userID
        self.username = username
        self.password = password

class Patient(User):
    def __init__(self, userID, username, password):
        super().__init__(userID, username, password)
        self.appointments = []
        self.history = []

    def submitReport(self, report):
        # Code to submit a report
        pass

    def reserveAppointment(self, doctor, date):
        # Code to reserve an appointment
        pass

    def viewDoctorLocation(self, doctor):
        # Code to view doctor's location on a map
        pass

    def callDoctor(self, doctor):
        # Code to initiate a call to a doctor in case of emergency
        pass

class Doctor(User):
    def __init__(self, userID, username, password):
        super().__init__(userID, username, password)
        self.appointments = []
        self.prescriptions = []
        self.assessments = []

    def writePrescription(self, patient, medication):
        # Code to write a prescription for a patient
        pass

    def writeAssessment(self, patient, assessmentText):
        # Code to write an assessment for a patient
        pass

class Appointment:
    def __init__(self, doctor, patient, date):
        self.appointmentID = str(uuid.uuid4())
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.status = "Pending"

    def approve(self):
        self.status = "Approved"

    def reject(self):
        self.status = "Rejected"

class Prescription:
    def __init__(self, doctor, patient, medication):
        self.prescriptionID = str(uuid.uuid4())
        self.doctor = doctor
        self.patient = patient
        self.date = datetime.now()
        self.medication = medication

class Report:
    def __init__(self, patient, image):
        self.reportID = str(uuid.uuid4())
        self.patient = patient
        self.date = datetime.now()
        self.image = image

class Assessment:
    def __init__(self, doctor, patient, assessmentText):
        self.assessmentID = str(uuid.uuid4())
        self.doctor = doctor
        self.patient = patient
        self.date = datetime.now()
        self.assessmentText = assessmentText
