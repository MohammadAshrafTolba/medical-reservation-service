from flask import Flask
import json
from app.routes import cancel_appointment
from flaskr import flaskr

def test_cancel_valid_appointment():
    app = Flask(__name__)
    handler = new PatientAppointmentHandler()
    client = app.test_client()
    url = '/cancel_appointment'
     mock_request_data = {
        'appointment_id' : 1
     }

    response = client.post(url, data=json.dumps(mock_request_data))

    assert response == {'status' : 'True'}
