from AppSrc.models import Doctor, specializations, db


class DoctorHandler:

    def get_doctors_by_specialization(self, specialization):
        if specialization not in specializations:
             return False
        doctors = db.session.query(Doctor).filter(Doctor.specialization == specialization)
        return doctors

