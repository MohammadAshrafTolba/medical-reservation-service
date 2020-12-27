"""
This file is responsible for routing requests to the appropriate handlers
"""

from app.init_app import app, api
from flask import render_template, request, jsonify
from appointment_handler import AppointmentHandler as a_handler
from specialization_handler import SpecializationHandler as s_handler
from patient_appointment_handler import PatientAppointmentHandler as pa_handler
from jsonify_response import appointment_jsonify, patient_appointments_jsonify

"""
@app.route('/')
def create_appointment():
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
    return jsonify(resp)
