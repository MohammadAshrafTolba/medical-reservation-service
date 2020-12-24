from models import Appointment
from init_app import db
import datetime

class AppointmentHandler:

    def get_all_free_appointments(self):
        free_appointments = db.session.query(Appointment).filter(Appointment.status == 'free')
        return free_appointments

    #def get_specific_doctor_free_appointments(self):



dt = datetime.datetime(2020, 11, 29, 12, 2)
appoint = Appointment(dr_id=2, start_date=dt, end_date=dt, status='reserved')
db.session.add(appoint)
db.session.commit()
handler = AppointmentHandler()
appoints = Appointment.query.filter(Appointment.status == 'free')

for appoint in appoints:
    print(appoint)