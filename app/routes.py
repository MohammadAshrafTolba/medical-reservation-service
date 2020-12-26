"""
This file is responsible for routing requests to the appropriate handlers
"""
"""
from app.init_app import app, api
from flask import render_template, request
from appointment_handler import AppointmentHandler as a_handler
from patient_appointment_handler import PatientAppointmentHandler as pa_handler
from jsonify_response import appointment_jsonify, patient_appointments_jsonify
import json

@app.route('/')
def create_appointment():
    handler = a_handler()
    # get required data from get/post request 
    resp = handler.get_all_free_appointments()
    resp = appointment_jsonify(resp)
    resp = resp[0]['data']
    return resp
    # talk to the appropriate db handler and recieve content

    # jsonify the above content to respond to the calling jquery function
"""