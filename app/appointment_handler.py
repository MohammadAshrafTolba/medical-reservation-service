from models import Appointment
from doctor_handler import DoctorHandler
from init_app import db, app
from flask import jsonify
from datetime import datetime
from sqlalchemy.sql import extract

class AppointmentHandler:

    def appointment_exists(self, appointment_id):
        exists = db.session.query(Appointment).filter(Appointment.appointment_id == appointment_id).scalar() is not None
        return exists

    def get_appointment_by_id(self, appointment_id):
        """
        brief        : gets a specific appointment from the Appointments table by id 
        param        : appointment_id -- int -- unique id for the selected appointment 
        constraint   : none
        throws       : none
        return       : appointment (can be null if no appointment by id found)
        """

        appointment = db.session.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
        return appointment

    def get_all_free_appointments(self):
        """
        brief        : gets all free appointments from the Appointments table
        param        : none
        constraint   : none
        throws       : none
        return       : list of all free appointments (can be null if no free appointments found)
        """

        free_appointments = db.session.query(Appointment).filter(Appointment.status == "free")
        return free_appointments

    def get_specific_doctor_free_appointments(self, dr_id):
        """
        brief        : gets all free appointments of a specific dr
        param        : dr_id -- int -- unique id of the dr
        constraint   : none
        throws       : none
        return       : list of the dr's free appointments (can be null if no free appointments found for this dr)
        """

        free_appointments = db.session.query(Appointment).filter(Appointment.status == 'free', Appointment.dr_id == dr_id).all()
        return free_appointments

    def change_appointment_status(self, appointment_id):
        """
        brief        : a utility function to toggle appointment's status (free->reserved amd vice versa)
        param        : appointment_id -- int -- unique id for the selected appointment
        constraint   : none
        throws       : none
        return       : true if successfuly toggled, false if not 
        """

        appointment = db.session.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

        if appointment is None:
            return False

        if appointment.status == "free":
            appointment.status = "reserverd"
        else:
            appointment.status = "free"
        db.session.commit()

        return True
    
    def get_free_appointment_with_start_date(self, start_date):
        """
        brief        : gets all free appointments with a specific start date
        param        : start_date -- datatime object -- required appointment start date to search for
        constraint   : none
        throws       : none
        return       : list of all free appointments within the given start date (can be null if no free appointments found)
        """

        free_appointments = db.session.query(Appointment).filter(extract('year', Appointment.start_date) == start_date.year,
                                                                 extract('month', Appointment.start_date) == start_date.month,
                                                                 extract('day', Appointment.start_date) == start_date.day,
                                                                 extract('hour', Appointment.start_date) == start_date.hour,
                                                                 extract('minute', Appointment.start_date) == start_date.minute)
        return free_appointments

    def get_nearest_appointment(self):
        """
        brief        : gets nearest appointment available today (time wise)
        param        : none
        constraint   : none
        throws       : none
        return       : nearset appointment today (can be null if no appointment found today)
        """
        
        now = datetime.now()        

        # get all free appointments available later today
        nearest_todays_appointment = db.session.query(Appointment).filter(extract('year', Appointment.start_date) == now.year,
                                                                          extract('month', Appointment.start_date) == now.month,
                                                                          extract('day', Appointment.start_date) == now.day,
                                                                          extract('hour', Appointment.start_date) >= now.hour,
                                                                          extract('minute', Appointment.start_date) >= now.minute,
                                                                          Appointment.status == 'free').order_by(extract('minute', Appointment.start_date)).first()
        
        return nearest_todays_appointment

    def add_appointment(self, dr_id, start_date, end_date):
        dr_handler = DoctorHandler()
        dr = dr_handler.get_doctor_by_id(dr_id)
        if dr is None:
            return False
        appointment = Appointment(dr_id=dr_id, start_date=start_date, end_date=end_date, status='free')
        db.session.add(appointment)
        db.session.commit()
        return True

    def remove_appointment(self, appointment_id):
        if not self.appointment_exists:
            return False
        appointment = self.get_appointment_by_id(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return True


# basic testing before moving to the testing team
"""
handler = AppointmentHandler()
free_appoints = handler.get_all_free_appointments()
print('----all free appointments----')
for appoint in free_appoints:
    print(appoint)

free_appoints_dr = handler.get_specific_doctor_free_appointments(2)
print('----all dr_id=2 free appointments----')
for appoint in free_appoints_dr:
    print(appoint)

datetime = datetime(2020, 12, 26, 2, 57)
free_appoints = handler.get_free_appointment_with_start_date(datetime)
print('----all free appointments with datatime = 2020, 12, 26, 2, 57----')
for appoint in free_appoints:
    print(appoint)

now = datetime.now()
nearest_appoint = handler.get_nearest_appointment()
print('----nearest appoints----')
print(nearest_appoint)

handler.change_appointment_status(1)
appoint = handler.get_appointment_by_id(1)
print('appoint status should be reserved')
print(appoint)
"""