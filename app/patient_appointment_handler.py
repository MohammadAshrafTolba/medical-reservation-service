from models import PatientAppointment
from appointment_handler import AppointmentHandler
from init_app import db, app
from datetime import datetime


class PatientAppointmentHandler:
    """
    brief   :   Handler for handling CRUD operations in the patient appointments table
    """

    def get_all_patient_appointments(self, patient_id):
        """
        brief        : receives a unique patient id and returns a list of the 
        param        : patient_id -- int -- unique id of the patient 
        constraint   : none
        throws       : none
        return       : patient_appointments -- a list of appointments of a specific patient
        """

        patient_appointments = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id).all()
        return patient_appointments

    def create_normal_appointment(self, patient_id, appointtment_id, sicknes, appointment_type):
        """
        brief        : creates a normal appointment 
        param        : patient_id -- int -- unique id of the patient
                       appointment_id -- int -- unique id for the selected appointment 
                       sickness -- string -- cause for this appointment
                       appointment_type -- string -- 'free' or 'reserved'
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly booked
                       False -- if appointment couldn't be booked
        """

        appointment_handler = AppointmentHandler()
        appointment = appointment_handler.get_appointment_by_id(appointtment_id).first()

        if appointment is None:
            return False

        patient_appointment = PatientAppointment(patient_id = patient_id,
                                                appointment_id = appointtment_id,
                                                sicknes = sicknes,
                                                appointment_type = appointment_type)
        
        # let the old appointment's status be reserved
        appointment.status = "reserved"
        db.session.add(patient_appointment)
        db.session.commit()

        return True

    def create_urgent_appointment(self, patient_id, sicknes, appointment_type):
        """
        brief        : books an urgent appointment, nearest appointment available today (time wise)
        param        : patient_id -- int -- unique id of the patient 
                       appointment_id -- int -- unique id for the selected appointment 
                       sickness -- string -- cause for this appointment
                       appointment_type -- string -- 'free' or 'reserved'
        constraint   : none
        throws       : none
        return       : True -- if appointment was successfuly booked
                       False -- if no appointments found
        """

        appointment_handler = AppointmentHandler()
        nearest_appointment_today = appointment_handler.get_nearest_appointment()

        if nearest_appointment_today is None:
            return False

        patient_appointment = PatientAppointment(patient_id = patient_id,
                                                 appointment_id = nearest_appoinment_today.appointtment_id,
                                                 sicknes = sicknes,
                                                 appointment_type = appointment_type)

        nearest_appointment_today.status = "reserved"
        db.session.add(patient_appointment)
        db.session.commit()

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
        appointment = appointment_handler.get_appointment_by_id(appointment_id).first()

        if appointment is None:
            return False

        patient_appointment = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id, 
                                                                          PatientAppointment.appointment_id == appointment_id)
        db.session.delete(patient_appointment)
        db.session.commit()

        # let the appointment's status be free again (in the Appointments table)
        appointment.status = "free"
        
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
        old_appointment = appointment_handler.get_appointment_by_id(old_appointment_id).first()
        
        if old_appointment is None:
            return False

        old_pateint_appointment = db.session.query(PatientAppointment).filter(PatientAppointment.appointment_id == old_appointment_id).first()
        
        # give the old_patient_appointment the new_appointment_id
        old_appointment.appointment_id = new_appointment_id
        db.session.commit()

        # toggle old appointment's and new appointment's status
        appointment_handler.change_appointment_status(old_appointment_id)
        appointment_handler.change_appointment_status(new_appointment_id)

        return True