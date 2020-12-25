from models import PatientAppointment
from appointment_handler import AppointmentHandler
from init_app import db, app


class PatientAppointmentHandler:

    def get_all_patient_appointments(self, patient_id):
        patient_appointments = db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id).all()
        return patient_appointments

    def create_appointment(self, patient_id, appointtment_id, sicknes, appointment_type):
        
        appointment_handler = AppointmentHandler()
        appointment = appointment_handler.get_appointment_by_id(appointtment_id).first()

        if appointment is None:
            return False

        patient_appointment = PatientAppointment(
                                                    patient_id = patient_id,
                                                    appointment_id = appointtment_id,
                                                    sicknes = sicknes,
                                                    appointment_type = appointment_type
                                                )
        db.session.add(patient_appointment)
        db.session.commit()
        
        # let the old appointment's status be reserved
        appointment_handler.change_appointment_status(appointtment_id)

        return True

    def delete_appointment(self, patient_id, appointment_id):

        appointment_handler = AppointmentHandler()
        appointment = appointment_handler.get_appointment_by_id(appointment_id).first()

        if appointment is None:
            return False

        db.session.query(PatientAppointment).filter(PatientAppointment.patient_id == patient_id, 
                                                    PatientAppointment.appointment_id == appointment_id)
        session.commit()

        # let the old appointment's status be free again
        appointment_handler.change_appointment_status(appointment_id)
        
        return True

    def update_appointment(self, old_appointment_id, new_appointment_id):
        
        appointment_handler = AppointmentHandler()
        appointment = appointment_handler.get_appointment_by_id(appointment_id).first()

        if appointment is None:
            return False

        old_appointment = db.session.query(PatientAppointment).filter(PatientAppointment.appointment_id == old_appointment_id).first()
        old_appointment.appointment_id = new_appointment_id
        db.session.commit()

        # let the old appointment's status be free again
        appointment_handler.change_appointment_status(old_appointment_id)

        return True