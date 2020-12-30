from models import PatientAppointment
from appointment_handler import AppointmentHandler
from patient_handler import PatientHandler
from init_app import db, app
from datetime import datetime


class PatientAppointmentHandler:
    """
    brief   :   Handler for handling CRUD operations in the patient appointments table
    """

    def patient_appointment_exists(self, patient_id, appointment_id):
        query = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id, PatientAppointment.appointment_id == appointment_id).scalar()
        exists = query is not None
        return exists

    def get_all_patient_appointments(self, patient_id):
        """
        brief        : receives a unique patient id and returns a list of the 
        param        : patient_id -- int -- unique id of the patient 
        constraint   : none
        throws       : none
        return       : patient_appointments -- a list of appointments of a specific patient
                       None -- if no such patient exists
        """
        p_handler = PatientHandler()
        if not p_handler.patient_exists(patient_id):
            return None
        patient_appointments = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id).all()
        return patient_appointments

    def create_normal_appointment(self, patient_id, appointment_id, patient_name, patient_email, patient_phone_number, patient_age, specialization):
        """
        brief        : creates a normal appointment 
        param        : patient_id -- int -- unique id of the patient
                       appointment_id -- int -- unique id for the selected appointment 
                       patient_name -- string, patient_email -- string
                       patient_phone_number -- int, patient_age -- int
                       specialization -- string -- cardiologist, dentist, ...etc
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly booked
                       False -- if appointment couldn't be booked
        """

        appointment_handler = AppointmentHandler()
        p_handler = PatientHandler()

        if not p_handler.patient_exists(patient_id) or not appointment_handler.appointment_exists(appointment_id):
            print("here1")
            return False

        appointment = appointment_handler.get_appointment_by_id(appointment_id)

        if appointment.status == "reserved":
            print("here2")
            return False

        if self.patient_appointment_exists(patient_id, appointment_id):
            print("here3")
            return False
        
        patient_appointment = PatientAppointment(patient_id = patient_id,
                                                 appointment_id = appointment_id,
                                                 patient_name = patient_name,
                                                 patient_age = patient_age,
                                                 patient_email = patient_email,
                                                 patient_phone_number = patient_phone_number,
                                                 specialization = specialization,
                                                 appointment_type = "normal")
        
        db.session.add(patient_appointment)
        db.session.commit()

        # let the appointment status be reserved
        appointment_handler.change_appointment_status(appointment_id)

        return True

    def create_urgent_appointment(self, patient_id, patient_name, patient_email, patient_phone_number, patient_age, specialization):
        """
        brief        : books an urgent appointment, nearest appointment available today (time wise)
        param        : patient_id -- int -- unique id of the patient 
                       appointment_id -- int -- unique id for the selected appointment
                       patient_name -- string, patient_email -- string
                       patient_phone_number -- int, patient_age -- int
                       specialization -- string -- dentist, cardiologist, ...etc
                       appointment_type -- string -- 'free' or 'reserved'
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly booked
                       False -- if no appointments found
        """

        p_handler = PatientHandler()
        if not p_handler.patient_exists(patient_id):
            return False

        appointment_handler = AppointmentHandler()
        nearest_appointment_today = appointment_handler.get_nearest_appointment()

        if nearest_appointment_today is None:
            return False

        if self.patient_appointment_exists(patient_id, nearest_appointment_today.appointment_id):
            return False

        patient_appointment = PatientAppointment(patient_id = patient_id,
                                                 appointment_id = nearest_appointment_today.appointment_id,
                                                 patient_name = patient_name,
                                                 patient_age = patient_age,
                                                 patient_email = patient_email,
                                                 patient_phone_number = patient_phone_number,
                                                 specialization = specialization,
                                                 appointment_type = "urgent")

        db.session.add(patient_appointment)
        db.session.commit()

        # toggle the appointment status to be reserved
        appointment_handler.change_appointment_status(nearest_appointment_today.appointment_id)

        return True

    def delete_appointment(self, patient_id, appointment_id):
        """
        brief        : cancels a specific appointment by id 
        param        : patient_id -- int -- unique id of the patient 
                       appointment_id -- int -- unique id for the selected appointment 
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly canceled
                       False -- if appointment couldn't be canceled
        """
        appointment_handler = AppointmentHandler()
        p_handler = PatientHandler()

        if not p_handler.patient_exists(patient_id) or not appointment_handler.appointment_exists(appointment_id):
            return False

        if not self.patient_appointment_exists(patient_id, appointment_id):
            return False

        patient_appointment = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id, 
                                                                          PatientAppointment.appointment_id == appointment_id).first()
        
        # check if patient has such an appointment
        if patient_appointment is None:
            return False

        db.session.delete(patient_appointment)
        db.session.commit()

        # let the appointment's status be free again (in the Appointments table)
        appointment_handler.change_appointment_status(appointment_id)

        return True

    def update_appointment(self, old_appointment_id, new_appointment_id):
        """
        brief        : updates/changes an appointment with another one (changing dates) 
        param        : old_appointment_id -- int -- unique id for the old appointment to be changed
                       new_appointment_id -- int -- unique id for the new appointment to be booked
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly updated
                       False -- if appointment couldn't be updated
        """

        appointment_handler = AppointmentHandler()
        old_appointment = appointment_handler.get_appointment_by_id(old_appointment_id)
        new_appointment = appointment_handler.get_appointment_by_id(new_appointment_id)

        if not appointment_handler.appointment_exists(old_appointment_id) or not appointment_handler.appointment_exists(old_appointment_id):
            return False

        old_pateint_appointment = db.session.query(PatientAppointment).filter(PatientAppointment.appointment_id == old_appointment_id).first()
        
        if old_pateint_appointment == None:
            return False

        # create the new appointment (with the new id)
        self.create_normal_appointment(old_pateint_appointment.patient_id,
                                       new_appointment_id,
                                       old_pateint_appointment.patient_name,
                                       old_pateint_appointment.patient_email,
                                       old_pateint_appointment.patient_phone_number,
                                       old_pateint_appointment.patient_age,
                                       old_pateint_appointment.specialization)
        
        # delete the old appointment
        self.delete_appointment(old_pateint_appointment.patient_id, old_appointment_id)

        return True

"""
# basic testing before moving to the testing team

handler = PatientAppointmentHandler()

p_appoints = handler.get_all_patient_appointments(1)
print('---p appoints for p_id=1---')
for p_appoint in p_appoints:
    print(p_appoint)


booked = handler.create_normal_appointment(1, 3, "zoox", "zoox@domain.com", None, 20, "cardiologist")
print('appointment (of id=3) booked? ', booked)
p_appoints = handler.get_all_patient_appointments(1)
print('---p appoints for p_id=1---')
for p_appoint in p_appoints:
    print(p_appoint)

deleted = handler.delete_appointment(1, 3)
print('appointment (of id=3) deleted? ', deleted)
print('---p appoints for p_id=1---')
p_appoints = handler.get_all_patient_appointments(1)
for p_appoint in p_appoints:
    print(p_appoint)

booked = handler.create_normal_appointment(1, 4, "zoox", "zoox@domain.com", None, 20, "cardiologist")
print('appointment (of id=4) booked? ', booked)
p_appoints = handler.get_all_patient_appointments(1)
print('---p appoints for p_id=1---')
for p_appoint in p_appoints:
    print(p_appoint)

updated  = handler.update_appointment(4, 3)
print('appointment updated from id=4 to id=3? ', updated)
p_appoints = handler.get_all_patient_appointments(1)
print('---p appoints for p_id=1---')
for p_appoint in p_appoints:
    print(p_appoint)

from datetime import datetime
from models import Appointment

now = datetime.now()
now = now.replace(hour = now.hour + 2)
appoint = Appointment(dr_id=1, start_date=now, end_date=now, status="free")

db.session.add(appoint)
db.session.commit()

booked = handler.create_urgent_appointment(1, "zoox", "zoox@domain.com", None, 20, "cardiologist")
print('appointment urgent appointment booked? ', booked)
p_appoints = handler.get_all_patient_appointments(1)
print('---p appoints for p_id=1---')
for p_appoint in p_appoints:
    print(p_appoint)
"""