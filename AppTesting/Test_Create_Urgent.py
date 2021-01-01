
import unittest
from datetime import datetime

from init_app import db
from patient_appointment_handler import PatientAppointmentHandler
from appointment_handler import AppointmentHandler
#from models import Patient, Doctor, Appointment, PatientAppointment


class test_create_urgent(unittest.TestCase):




#passed
    def test_001(self):
        appointment_id = 600
        now = datetime.now()

        a_handler = AppointmentHandler()
        a_handler.add_appointment(appointment_id, 1, now, now)
       
        pa_handler = PatientAppointmentHandler()
        answer = pa_handler.create_urgent_appointment(1, "mohamed", "mohamed@gmail.com", 1235, 35, "dermatologist")
        
        a_handler.remove_appointment(appointment_id)

        self.assertTrue(answer)

if __name__ == "__main__":
    unittest.main()

