"""
This file is responsible for routing requests to the appropriate handlers
"""

from app.init_app import app
from flask import render_template, request, jsonify
from appointment_handler import AppointmentHandler as a_handler
from specialization_handler import SpecializationHandler as s_handler
from patient_appointment_handler import PatientAppointmentHandler as pa_handler
from doctor_handler import DoctorHandler as d_handler
from jsonify_response import appointment_jsonify, patient_appointments_jsonify, doctors_jsonify


"""
@app.route('/')
def create_appointment_page():
    return render_template('/Html/NormalCreation.html')
"""

@app.route('/specialization')
def get_specializations():
    handler = s_handler()
    resp = handler.get_specializations()
    if resp is None:
        resp = {'data' : 'none'}
    else:
        resp = {'data' : resp}
    print(resp)
    return jsonify(resp)

@app.route('/doctors')
def get_doctors():
    print('yooooooo')
    specialization = 'dentist'
    #specialization = request.args['specialization']
    handler = d_handler()
    _, resp = handler.get_doctors_by_specialization(specialization)
    resp = doctors_jsonify(resp)
    return resp

@app.route('/dr_appointments')
def get_dr_appointments():
    # should get dr id here from the request body
    dr_id = 2
    handler = a_handler()
    resp = handler.get_specific_doctor_free_appointments(dr_id)
    resp = appointment_jsonify(resp)
    return resp

@app.route('/normal_appointment')
def create_normal_appointment_by_id():
    appointment_id = 4
    patient_id = 1
    patient_name = 'ashraf'
    patient_age = 30
    patient_email = 'ashraf@domain.com'
    patient_phone_number = None
    specialization = 'dentist'

    handler = pa_handler()
    resp = handler.create_normal_appointment(patient_id, appointment_id, patient_name, patient_email, patient_phone_number, patient_age, specialization)
    return jsonify({'status' : str(resp)})

@app.route('/urgent_appointment')
def create_urgent_appointment():
    patient_id = 1
    patient_name = 'ashraf'
    patient_age = 30
    patient_email = 'ashraf@domain.com'
    patient_phone_number = None
    specialization = 'dentist'

    handler = pa_handler()
    resp = handler.create_urgent_appointment(patient_id, patient_name, patient_email, patient_phone_number, patient_age, specialization)
    return jsonify({'status' : str(resp)})

@app.route('/retrieve_patient_appointments')
def get_all_patient_appointment():
    patient_id = 1

    handler = pa_handler()
    resp = handler.get_all_patient_appointments(patient_id)
    resp = patient_appointments_jsonify(resp)
    return resp

@app.route('/update_appointment')
def update_appointment():
    old_appointment_id = 1
    new_appointment_id = 2

    handler = pa_handler()
    resp = handler.update_appointment(old_appointment_id, new_appointment_id)
    return jsonify({'status' : str(resp)})

@app.route('/cancel_appointment')
def cancel_appointment():
    patient_id = 1
    appointment_id = 2

    handler = pa_handler()
    resp = handler.delete_appointment(patient_id, appointment_id)
    return jsonify({'status' : str(resp)})