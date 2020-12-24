from models import Appointment
from init_app import db
import datetime

class AppointmentHandler:

    def get_all_free_appointments(self):
        free_appointments = Appointment.query.filter(Appointment.status == 'free')
        return free_appointments

    def get_specific_doctor_free_appointments(self, dr_id):
        free_appointments = Appointment.query.filter(Appointment.status == 'free', Appointment.dr_id == dr_id)
        return free_appointments


"""
dt = datetime.datetime(2020, 11, 29, 12, 2)
appoint = Appointment(dr_id=1, start_date=dt, end_date=dt, status='free')
db.session.add(appoint)
db.session.commit()
handler = AppointmentHandler()
"""
appoints = Appointment.query.filter(Appointment.status == 'free', Appointment.dr_id == 1)

for appoint in appoints:
    print(appoint.appointment_id)