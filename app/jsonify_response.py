from models import AppointmentSchema as a_schema, PatientAppointmentSchema as pa_schema, DoctorSchema as d_schema
from flask import jsonify
import json


def appointment_jsonify(appointments):
    if appointments is None or not appointments:
        return jsonify({'data' : 'none'})

    appointments_schema = a_schema(many=True)
    json_response = appointments_schema.dump(appointments)

    return jsonify({'data' : json_response})

def patient_appointments_jsonify(p_appointments):
    if appointments is None:
        return jsonify({'data' : 'none'})

    patient_appointments_schema = pa_schema(many=True)
    json_response = patient_appointments_schema.dump(p_appointments)

    return jsonify({'data' : json_response})

def doctors_jsonify(doctors):
    if doctors is None:
        return jsonify({'data' : 'none'})

    doctors_schema = d_schema(many=True)
    json_response = doctors_schema.dump(doctors)

    return jsonify({'data' : json_response})

