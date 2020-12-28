from models import Doctor, specializations, db


class DoctorHandler:

    def doctor_exists(self, dr_id):
        exists = db.session.query(Doctor).filter(Doctor.id == dr_id).scalar() is not None
        return exists

    def get_doctors_by_specialization(self, specialization):
        if specialization not in specializations:
            return False, None
        doctors = db.session.query(Doctor).filter(Doctor.specialization ==specialization).all()
        return True, doctors

    def get_doctor_by_id(self, dr_id):
        if self.doctor_exists(dr_id):
            dr = db.session.query(Doctor).filter(Doctor.id == dr_id).scalar()
            return dr
        return None