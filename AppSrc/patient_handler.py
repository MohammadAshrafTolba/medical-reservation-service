from models import db, Patient


class PatientHandler:

    def patient_exists(delf, patient_id):
        exists = db.session.query(Patient).filter(Patient.id == patient_id).scalar is not None
        return exists