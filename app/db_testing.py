from init_app import db
from models import Patient, Doctor, Appointment
import datetime


#db.drop_all()
#db.create_all()

patient1 = Patient(name="patient1", age=32, email="patient1@gmail.com")
#print(app.logger.info(patient1.id))
db.session.add(patient1)
db.session.commit()

patient2 = Patient(name="patient2", age=34, email="patient2@gmail.com")
#print(app.logger.info(patient1.id))
db.session.add(patient2)
db.session.commit()

#print(app.logger.info(patient1.id))
l = Patient.query.all()
print(l)

dr1 = Doctor(name='mark', specialization='dentist')
db.session.add(dr1)
db.session.commit()

dr2 = Doctor(name='markk', specialization='dentist')
db.session.add(dr2)
db.session.commit()

l = Doctor.query.all()
print(l)

dt = datetime.datetime(2020, 11, 29, 12, 2)     # year, month, day, hours, minutes
#print(dt)
appoint = Appointment(dr_id=2, start_date=dt, end_date=dt, status='free')
db.session.add(appoint)
db.session.commit()
l = Appointment.query.all()
print(l)