"""
This file is for creating the database tables using sqlalchemy object 'db'
"""

from init_app import db, app, ma
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship


specializations = ['dentistry', 'dermatology']

class Patient(db.Model):
    """
    brief : db table for storing patients' data
    """

    __tablename__ = "patient"
    
    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120))
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):     # This method defines how objects should be printed
        return '<patient: id: {0}, name: {1}, age: {2}>'.format(self.id, self.name, self.age)

class Doctor(db.Model):
    """
    brief : db table for storing doctors' data
    """

    __tablename__ = "doctor"
    
    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(20), nullable=False)

    def __repr__(self):     # This method defines how objects should be printed
        return '<doctor: id: {0}, name: {1}, specialization: {2}>'.format(self.id, self.name, self.specialization)

class Appointment(db.Model):
    """
    brief : db table for storing all appointments on the system (can be free or reserved appointments)
    """

    __tablename__ = 'appointment'
    
    appointment_id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    dr_id = db.Column(db.Integer, ForeignKey('doctor.id'))
    start_date = db.Column(DateTime, index=True, nullable=False)
    end_date = db.Column(DateTime, index=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    dr = relationship('Doctor', foreign_keys=[dr_id])

    def __repr__(self):     # This method defines how objects should be printed
        return '<appointment: id: {0}, dr_id: {1}, start_date: {2}, end_date: {3}, status: {4}>'.format(self.appointment_id, self.dr_id, self.start_date, self.end_date, self.status)

class PatientAppointment(db.Model):
    """
    brief : db table for storing appointments that patients have made
    """

    __tablename__ = 'patient_appointment'

    patient_id = db.Column(db.Integer, ForeignKey('patient.id'), nullable=False, primary_key=True)
    appointment_id = db.Column(db.Integer, ForeignKey('appointment.appointment_id'), nullable=False, primary_key=True)
    specialization = db.Column(db.String(20), nullable=True)
    appointment_type = db.Column(db.String(20), nullable=False)

    patient = relationship('Patient', foreign_keys=[patient_id])
    appointment = relationship('Appointment', foreign_keys=[appointment_id])
    
    def __repr__(self):     # This method defines how objects should be printed
        return '<Patient Appointment: patient_id: {0}, appointment_id: {1}>'.format(self.patient_id, self.appointment_id)


"""
    The following tables are used later to map query results to json objects
"""

class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment

class PatientAppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PatientAppointment
