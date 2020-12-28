"""
This file is responsible for routing requests to the appropriate handlers
"""

from AppSrc.init_app import app, api
from flask import render_template, request, jsonify
from AppSrc.specialization_handler import SpecializationHandler as s_handler
from AppSrc.patient_appointment_handler import PatientAppointmentHandler as pa_handler
from AppSrc.jsonify_response import appointment_jsonify, patient_appointments_jsonify

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
