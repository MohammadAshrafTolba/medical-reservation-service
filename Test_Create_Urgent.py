
import unittest
from datetime import datetime

from init_app import db
from patient_appointment_handler import PatientAppointmentHandler
from models import Patient, Doctor, Appointment, PatientAppointment


class test_create_urgent(unittest.TestCase):
    now = datetime.now()

    appoint = Appointment(dr_id=2, start_date=now, end_date=now, status='free')
    db.session.add(appoint)
    db.session.commit()
    now = now.replace(hour=4)
    appoint = Appointment(dr_id=2, start_date=now, end_date=now, status='free')
    db.session.add(appoint)
    db.session.commit()



#passed
    def test_001(self):
        obj=PatientAppointmentHandler
        answer=obj.create_urgent_appointment(self,1,"dermatologist")
        self.assertTrue(answer)