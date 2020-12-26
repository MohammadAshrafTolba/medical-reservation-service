"""
This file is responsible for routing requests to the appropriate handlers
"""

from init_app import app, api
from flask import render_template, request
#from appointment_handler import AppointmentHandler as a_handler
#from patient_appointment_handler import PatientAppointmentHandler as pa_handler
#from jsonify_response import appointment_jsonify, patient_appointments_jsonify

"""
@app.route('/create_appointment')
def create_appointment():

    # get required data from get/post request 

    # talk to the appropriate db handler and recieve content

    # jsonify the above content to respond to the calling jquery function

    pass
"""