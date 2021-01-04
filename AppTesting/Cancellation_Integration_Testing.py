from flask import Flask
import json
from app.routes import cancel_appointment
from flaskr import flaskr
import pytest

@pytest.fixture
def client():
    db_fd, flaskr.app.config['routes'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            flaskr.init_app()
        yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['routes'])

def test_cancel_valid_appointment():
    app = Flask(__name__)
    handler = new PatientAppointmentHandler()
    client = flaskr.app.test_client()
    url = '/cancel_appointment'
     mock_request_data = {
        'appointment_id' : 1
     }

    response = client.post(url, data=json.dumps(mock_request_data))

    assert response == {'status' : 'True'}
