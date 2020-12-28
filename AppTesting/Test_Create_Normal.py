"""import unittest
from patient_appointment_handler import PatientAppointmentHandler

class MyTestCase(unittest.TestCase):

    def test_createapp(self):

        answer = PatientAppointmentHandler.create_normal_appointment(self, 123, 159, "cold");
        self.assertEqual(answer, True);


if __name__ == '__main__':
    unittest.main()
    """
import unittest
from datetime import datetime

from AppSrc.init_app import db
from AppSrc.patient_appointment_handler import PatientAppointmentHandler
from AppSrc.models import Patient, Doctor, Appointment, PatientAppointment




class test_create(unittest.TestCase):


#passed
    def test_create_normal_app001(self):
        obj = PatientAppointmentHandler
        answer = obj.create_normal_appointment(self,15, 9, "cardiologist")
        self.assertEqual(True,answer)




#passed
#invalid app_ID
    def test_create_normal_app002(self):
        obj1 = PatientAppointmentHandler
        answer1 = obj1.create_normal_appointment(self,19, 22, "cardiologist")
        self.assertEqual(False,answer1)







''' 
#ffffffff
    # invalid Patient_ID
   def test_create_normal_app002(self):
        obj = PatientAppointmentHandler
        answer = obj.create_normal_appointment(self,20, 8, "cardiologist")
        self.assertEqual(False,answer)

'''

