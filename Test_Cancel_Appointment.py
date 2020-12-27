import unittest 
from patient_appointment_handler import PatientAppointmentHandler
from models import Appointment , Doctor , PatientAppointment

"""
query = PatientAppointment.query.all()

for i in query:
    print(i)
"""

class TestCancellation(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_valid_user_id(self):
        obj = PatientAppointmentHandler()
        x = obj.delete_appointment(1,3)
        self.assertEqual(x,True)

    def test_invalid_user_id(self):
        obj = PatientAppointmentHandler()
        x = obj.delete_appointment(3,3)
        self.assertEqual(x,False)

    def test_invalid_appointment_id(self):
        obj = PatientAppointmentHandler()
        x = obj.delete_appointment(1,10)
        self.assertEqual(x,False)

  
if __name__ == '__main__': 
    unittest.main() 