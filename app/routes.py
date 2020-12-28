"""
This file is responsible for routing requests to the appropriate handlers
"""
import sys
sys.path.append('.')
sys.path.append('../')


from init_app import app, api
from flask import render_template, request, jsonify
from appointment_handler import AppointmentHandler as a_handler
from specialization_handler import SpecializationHandler as s_handler
from patient_appointment_handler import PatientAppointmentHandler as pa_handler
from doctor_handler import DoctorHandler as d_handler
from jsonify_response import appointment_jsonify, patient_appointments_jsonify, doctors_jsonify


@app.route('/')
def create_appointment():
    return render_template('/Html/NormalCreation.html')


@app.route('/specialization')
def get_specializations():
    handler = s_handler()
    resp = handler.get_specializations()
    if resp is None:
        resp = {'data' : 'none'}
    else:
        resp = {'data' : resp}
    return jsonify(resp)

@app.route('/doctors')
def get_doctors():
    specialization = request.args['specialization']
    handler = d_handler()
    _, resp = handler.get_doctors_by_specialization(specialization)
    resp = doctors_jsonify(resp)
    return resp

@app.route('/dr_appointments')
def get_dr_appointments():
    dr_id = 1
    handler = a_handler()
    resp = handler.get_specific_doctor_free_appointments(dr_id)
    resp = appointment_jsonify(resp)
    return resp

@app.route('/normal_appointment')
def create_normal_appointment_by_id():
    patient_id = 1
    appointment_id = 4
    specialization = 'dentist'

    handler = pa_handler()
    resp = pa_handler.create_normal_appointment(patient_id, appointment_id, specialization)
    return jsonify({'status' : resp})

