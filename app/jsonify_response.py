from models import AppointmentSchema as a_schema, PatientAppointmentSchema as pa_schema


def appointment_jsonify(appointments):
    if appointments is None or len(appointments) == 0:
        return {'data' : 'none'}

    appointments_schema = a_schema(many=True)
    json_response = appointments_schema.dump(appointments)

    return {'data' : json_response}

def patient_appointments_jsonify(appointments):
    if appointments is None or len(appointments) == 0:
        return {'data' : 'none'}

    patient_appointments_schema = pa_schema(many=True)
    json_response = patient_appointments_schema.dump(appointments)

    return {'data' : json_response}
