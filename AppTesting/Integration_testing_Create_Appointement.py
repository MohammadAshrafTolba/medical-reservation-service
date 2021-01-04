


from init_app import db
from models import  Appointment,Doctor
from datetime import datetime



appoints = Appointment.query.all()

print('---appoints---')
for appoint in appoints:
    print(appoint)