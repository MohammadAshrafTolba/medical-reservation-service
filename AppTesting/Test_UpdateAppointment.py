import unittest
from mock import patch, Mock

from AppSrc.appointment_handler import AppointmentHandler
from AppSrc.patient_appointment_handler import PatientAppointmentHandler


class TestUpdateAppointment(unittest.TestCase):

    def setUp(self):
        # Test Constants
        self.AppointmentID = 75
        self.ExtraAppointmentID = 76
        self.NewAppointmentID = 80
        self.PatientID = 15
        self.Spec = "dentist"

        # Handlers Init
        self.aHandler = AppointmentHandler()
        self.pHandler = PatientAppointmentHandler()

        # Delete the Appointment for this Patient if exists
        pList = self.pHandler.get_all_patient_appointments(self.PatientID)
        for i in pList:
            if i.appointment_id == self.AppointmentID:
                self.pHandler.delete_appointment(self.PatientID, self.AppointmentID)
            if i.appointment_id == self.NewAppointmentID:
                self.pHandler.delete_appointment(self.PatientID, self.NewAppointmentID)

        self.pHandler.delete_appointment(self.PatientID, self.AppointmentID)
        self.pHandler.delete_appointment(self.PatientID, self.NewAppointmentID)


    def tearDown(self):
        pass

    def test_NormalUpdate1(self):
        """
        Test for Normal Update
        Create Normal Appointment and update it "Check For Function Return Values"
        """

        bRet = self.pHandler.create_normal_appointment(self.PatientID, self.AppointmentID, self.Spec)
        self.assertEqual(bRet, True)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)
        self.assertTrue(bRet)

    def test_NormalUpdate2(self):
        """
        Test for Normal Update
        Create Normal Appointment and update it "Check The Old Appointment ID in the DB"
        """

        bRet = self.pHandler.create_normal_appointment(self.PatientID, self.AppointmentID, self.Spec)
        self.assertEqual(bRet, True)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)
        self.assertTrue(bRet)

        # Check For The Old Appointment in the DB
        pList = self.pHandler.get_all_patient_appointments(self.PatientID)
        foundAppointment = False
        for i in pList:
            if i == self.AppointmentID:
                foundAppointment = True

        if foundAppointment:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


    def test_NormalUpdate3(self):
        """
        Test for Normal Update
        Create Normal Appointment and update it "Check The NewAppointment ID in the DB"
        """

        bRet = self.pHandler.create_normal_appointment(self.PatientID, self.AppointmentID, self.Spec)
        self.assertTrue(bRet)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)
        self.assertTrue(bRet)

        # Check For The New Appointment in the DB
        pList = self.pHandler.get_all_patient_appointments(self.PatientID)
        foundAppointment = False
        for i in pList:
            if i == self.NewAppointmentID:
                foundAppointment = True

        if not foundAppointment:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


    @patch('AppSrc.appointment_handler.AppointmentHandler.get_nearest_appointment')
    def test_UrgentUpdate1(self, mock_get_nearest_appointment):
        """
        Test Urgent Appointment Update "Should Not Update"
        Create An Urgent Appointment then Update it "Only check for function returns values"
        """

        # Mock Object To Return Expected Results
        mock_Obj = Mock()
        mock_Obj.appointment_id = self.AppointmentID
        mock_get_nearest_appointment.return_value = mock_Obj

        bRet = self.pHandler.create_urgent_appointment(self.PatientID, "dentist")
        # It Should Pass "Prerequisite For Update Urgent Appointment Test"
        self.assertEqual(bRet, True)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)

        # It Should Not Pass
        self.assertEqual(bRet, False)


    @patch('AppSrc.appointment_handler.AppointmentHandler.get_nearest_appointment.appointment_id')
    def test_UrgentUpdate2(self, mock_get_nearest_appointment):
        """
        Test Urgent Appointment Update "Should Not Update"
        Create an appointment then update it "check for the old appointment in the DB"
        """

        # Mock Object To Return Expected Results
        mock_Obj = Mock()
        mock_Obj.appointment_id = self.AppointmentID
        mock_get_nearest_appointment.return_value = mock_Obj

        bRet = self.pHandler.create_urgent_appointment(self.PatientID, self.Spec)
        # It Should Pass "Prerequisite For Update Urgent Appointment Test"
        self.assertEqual(bRet, True)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)

        # It Should Not Pass
        self.assertEqual(bRet, False)

        # Check For The Old Appointment in the DB
        pList = self.pHandler.get_all_patient_appointments(self.PatientID)
        foundAppointment = False
        for i in pList:
            if i == self.AppointmentID:
                foundAppointment = True

        if not foundAppointment:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


    @patch('AppSrc.appointment_handler.AppointmentHandler.get_nearest_appointment.appointment_id')
    def test_UrgentUpdate3(self, mock_get_nearest_appointment):
        """
        Test Urgent Appointment Update "Should Not Update"
        Create an appointment then update it "check for the new appointment in the DB"
        """

        # Mock Object To Return Expected Results
        mock_Obj = Mock()
        mock_Obj.appointment_id = self.AppointmentID
        mock_get_nearest_appointment.return_value = mock_Obj

        bRet = self.pHandler.create_urgent_appointment(self.PatientID, self.Spec)
        # It Should Pass "Prerequisite For Update Urgent Appointment Test"
        self.assertEqual(bRet, True)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)

        # It Should Not Pass
        self.assertEqual(bRet, False)

        # Check For The New Appointment in the DB
        pList = self.pHandler.get_all_patient_appointments(self.PatientID)
        for i in pList:
            if i == self.NewAppointmentID:
                self.assertTrue(False)

        self.assertTrue(True)


    def test_NormalUpdateNotCreatedAppointment(self):
        """
        Test Update For non-created appoinment
        """

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.NewAppointmentID)
        self.assertFalse(bRet)


    def test_NormalUpdate2CreatedAppointment(self):
        """
        Test Update For create 2 normal appointment and update one with the other appointment time
        """

        bRet = self.pHandler.create_normal_appointment(self.PatientID, self.AppointmentID, self.Spec)
        self.assertTrue(bRet)

        bRet = self.pHandler.create_normal_appointment(self.PatientID, self.ExtraAppointmentID, self.Spec)
        self.assertTrue(bRet)

        bRet = self.pHandler.update_appointment(self.AppointmentID, self.ExtraAppointmentID)
        self.assertFalse(bRet)

if __name__ == '__main__':
    unittest.main()
