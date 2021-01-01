

import unittest
from datetime import datetime

from app.init_app import db
from app.patient_appointment_handler import PatientAppointmentHandler
from app.appointment_handler import AppointmentHandler
#from app.models import Patient, Doctor, Appointment, PatientAppointment


class test_create(unittest.TestCase):

#passed
    def test_create_normal_app001(self):
        
        # specifying appointment_id that most probably isn't in the system
        appointment_id = 500
        now = datetime.now()

        a_handler = AppointmentHandler()
        a_handler.add_appointment(appointment_id, 1, now, now)
        
        pa_handler = PatientAppointmentHandler()
        
        # parameters needed for the create_normal_appointment_function
        # patient_id, appointment_id, patient_name, patient_email, patient_phone_number, patient_age, specialization

        answer = pa_handler.create_normal_appointment(1, appointment_id,"Ahmed","ahmed@gmail.com", 123, 25, "cardiologist")
        
        # remove the appointment created in order for the test to run OK every time
        a_handler.remove_appointment(appointment_id)

        self.assertEqual(True, answer)


if __name__ == '__main__':
    unittest.main()
