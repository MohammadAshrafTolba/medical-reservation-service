from models import Appointment, AppointmentSchema
from init_app import db, app
from flask import jsonify


class AppointmentHandler:

    def get_appointment_by_id(self, appointment_id):
        appointment = db.session.query(Appointment).filter(Appointment.appointment_id == appointment_id)
        return appointment

    def get_all_free_appointments(self):
        free_appointments = db.session.query(Appointment).all()
        return free_appointments

    def get_specific_doctor_free_appointments(self, dr_id):
        free_appointments = db.session.query(Appointment).filter(Appointment.status == 'free', Appointment.dr_id == dr_id)
        return free_appointments

    def change_appointment_status(self, appointment_id):
        appointment = db.session.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

        if appointment is None:
            return False

        if appointment.status == "free":
            appointment.status = "reserverd"
        else:
            appointment.status = "free"
        db.session.commit()

        return True
    
    def get_free_appointment_with_start_date(self, start_date):
        free_appointments = db.session.query(Appointment).filter(Appointment.start_date == start_date)
        return free_appointments


"""
handler = AppointmentHandler()
print(handler.get_all_free_appointments())
#print(handler.change_appointment_status(1))
"""