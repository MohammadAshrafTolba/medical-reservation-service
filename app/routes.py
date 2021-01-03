"""
This file is responsible for routing requests to the appropriate handlers
"""

from app.init_app import app
from flask import render_template, request, jsonify, session
from appointment_handler import AppointmentHandler as a_handler
from specialization_handler import SpecializationHandler as s_handler
from patient_appointment_handler import PatientAppointmentHandler as pa_handler
from doctor_handler import DoctorHandler as d_handler
from jsonify_response import appointment_jsonify, patient_appointments_jsonify, doctors_jsonify



@app.route('/')
@app.route('/Home.html')
def home_page():
    return render_template('Home.html')

@app.route('/NormalCreation.html')
def normal_creation_page():
    return render_template('NormalCreation.html')

@app.route('/UrgentCreation.html')
def urgent_creation_page():
    return render_template('UrgentCreation.html')

@app.route('/CancelForm.html')
def cancel_appointment_page():
    return render_template('CancelForm.html')

@app.route('/UpdateForm.html')
def get_update_scenario_1():
    return render_template('UpdateForm.html')

@app.route('/specialization')
def get_specializations():
    handler = s_handler()
    resp = handler.get_specializations()
    if resp is None:
        resp = {'data' : 'none'}
    else:
        resp = {'data' : resp}
    #print(resp)
    return jsonify(resp)

@app.route('/dr_by_appointment_id')
def get_dr_by_appointment_id():
    appointment_id = request.args['appointment_id']
    handler = a_handler()
    if not handler.appointment_exists(appointment_id):
        return jsonify({'data' : 'none'})
    appointment = handler.get_appointment_by_id(appointment_id)
    return jsonify({'data' : appointment.dr_id})

@app.route('/doctors')
def get_doctors():
    patient_id = 1
    option = int(request.args['option'])
    resp = None
    if option == 0:
        specialization = request.args['specialization']
        print(specialization)
        handler = d_handler()
        _, resp = handler.get_doctors_by_specialization(specialization)
        #print(resp)
    elif option == 1:
        appointment_id = request.args['appointment_id']
        handler = pa_handler()
        if appointment_id is None or not handler.patient_appointment_exists(patient_id, appointment_id):
            return jsonify({'data' : 'none'})
        appointment = handler.get_patient_appointment_by_id(appointment_id)
        #print(appointment)
        handler = d_handler()
        _, resp = handler.get_doctors_by_specialization(appointment.specialization)

    resp = doctors_jsonify(resp)
    return resp

@app.route('/dr_appointments')
def get_dr_appointments():
    handler = a_handler()
    option = int(request.args['option'])
    if option == 0:
        dr_id = request.args['dr_id']
        resp = handler.get_specific_doctor_free_appointments(dr_id)
        resp = appointment_jsonify(resp)
        return resp
    elif option == 1:
        appointment_id = request.args['appointment_id']
        dr_appointments = handler.get_specific_dr_appointments_by_appointment_id(appointment_id)
        resp = appointment_jsonify(dr_appointments)
        return resp

@app.route('/normal_appointment', methods=['POST'])
def create_normal_appointment_by_id():
    patient_id = 1
    appointment_id = request.form.get('appointment_id')
    patient_name = request.form.get('patient_name')
    patient_age = request.form.get('patient_age')
    patient_email = request.form.get('patient_email')
    patient_phone_number = request.form.get('patient_phone_number')
    specialization = request.form.get('specialization')

    handler = pa_handler()
    resp = handler.create_normal_appointment(patient_id, appointment_id, patient_name, patient_email, patient_phone_number, patient_age, specialization)
    return jsonify({'status' : str(resp)})

@app.route('/urgent_appointment', methods=['POST'])
def create_urgent_appointment():
    patient_id = 1
    patient_name = request.form.get('patient_name')
    patient_age = request.form.get('patient_age')
    patient_email = request.form.get('patient_email')
    patient_phone_number = request.form.get('patient_phone_number')
    specialization = request.form.get('specialization')

    handler = pa_handler()
    resp = handler.create_urgent_appointment(patient_id, patient_name, patient_email, patient_phone_number, patient_age, specialization)
    return jsonify({'status' : str(resp)})

@app.route('/retrieve_patient_normal_appointments')
def get_all_patient_appointment():
    patient_id = 1

    handler = pa_handler()
    resp = handler.get_all_patient_normal_appointments(patient_id)
    resp = patient_appointments_jsonify(resp)
    return resp

@app.route('/update_appointment', methods=['POST'])
def update_appointment():
    old_appointment_id = request.form.get('old_appointment_id')
    new_appointment_id = request.form.get('new_appointment_id')
    handler = pa_handler()
    resp = handler.update_appointment(old_appointment_id, new_appointment_id)
    print(resp)
    return jsonify({'status' : str(resp)})

@app.route('/cancel_appointment', methods=['POST'])
def cancel_appointment():
    patient_id = 1
    appointment_id = request.get_json(force=True).get('appointment_id')
    print(appointment_id)
    handler = pa_handler()
    resp = handler.delete_appointment(patient_id, appointment_id)
    return jsonify({'status' : str(resp)})