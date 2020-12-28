from init_app import db
from models import Patient, Doctor, Appointment, PatientAppointment
from datetime import datetime


db.drop_all()
db.create_all()


patient1 = Patient(name="patient1", age=32, email="patient1@gmail.com")
db.session.add(patient1)
db.session.commit()

patient2 = Patient(name="patient2", age=34, email="patient2@gmail.com")
db.session.add(patient2)
db.session.commit()

patients = Patient.query.all()

print('---patients---')
for patient in patients:
    print(patient)

dr1 = Doctor(name='mark', specialization='dentist')
db.session.add(dr1)
db.session.commit()

dr2 = Doctor(name='andy', specialization='cardiologist')
db.session.add(dr2)
db.session.commit()

drs = Doctor.query.all()

print('---drs---')
for dr in drs:
    print(dr)

dt1 = datetime(2020, 11, 29, 12, 2)     # year, month, day, hours, minutes
dt2 = datetime(2020, 11, 29, 3, 2)

appoint1 = Appointment(dr_id=1, start_date=dt1, end_date=dt2, status='reserved')
dt = datetime(2020, 11, 29, 12, 6)
appoint2 = Appointment(dr_id=2, start_date=dt1, end_date=dt2, status='reserved')

db.session.add(appoint1)
db.session.add(appoint2)
db.session.commit()

appoints = Appointment.query.all()

print('---appoints---')
for appoint in appoints:
    print(appoint)

#p_appointment1 = PatientAppointment(patient_id=2, appointment_id=1, sickness="cold", appointment_type="normal")
#db.session.add(p_appointment1)
#db.session.commit()
#p_appoints = PatientAppointment.query.all()

#print('---p appoints---')
#for appoint in p_appoints:
#    print(appoint)

now = datetime.now()

appoint = Appointment(dr_id=2, start_date=now, end_date=now, status='free')
db.session.add(appoint)
db.session.commit()
now = now.replace(hour = 4)
appoint = Appointment(dr_id=2, start_date=now, end_date=now, status='free')
db.session.add(appoint)
db.session.commit()

appoints = Appointment.query.all()

print('---appoints again---')
for appoint in appoints:
    print(appoint)
