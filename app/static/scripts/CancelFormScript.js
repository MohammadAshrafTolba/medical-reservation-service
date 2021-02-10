//prevent submit from refreshing
var form = document.getElementById("cancelForm");

function handleForm(event) {
    event.preventDefault();
}
form.addEventListener('submit', handleForm);

// Get appointments request
window.onload = function() {
    //todo patientId?
    var patientId = "1";
    getAppointments(patientId);
    //            mockGetAppointments();
};

var dropdownList = document.getElementById("dropdown");

mockGetAppointments = function() {
    var opt = document.createElement('option');
    opt.appendChild(document.createTextNode('appointment 1'));
    opt.value = 'appointment 1';
    dropdownList.appendChild(opt);
}


/* *
 * @brief        : sends post request to get appointments
 * @param        : patientId
 * @constrant    : none
 * @throws       : none
 * @return       : none
 * */
getAppointments = function(patientId) {
    var xhr = new XMLHttpRequest();
    var url = "/retrieve_all_patient_appointments";

    xhr.open("GET", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            //console.log(xhr.responseText)
            var json = JSON.parse(xhr.responseText);
            json = json['data'];
            if (json != 'none') {
                var appoint = "";
                //var appendData = "";
                for (var i = 0; i < json.length; ++i) {
                    appoint = json[i];
                    //console.log(appoint);
                    var opt = document.createElement('option');
                    opt.textContent = 'appointment id: ' + appoint['appointment_id'] + " - patient's name: " + appoint['patient_name'] + " - dr's spec: " + appoint['specialization'];
                    opt.value = appoint['appointment_id'];
                    dropdownList.appendChild(opt);
                }
            }
        }
    };
    
    var data = JSON.stringify({
        //"patient_id": patientId
    });
    xhr.send(data);
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("submit");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var modalText = document.getElementById("modalText");

/* *
 * @brief        : sends post request to cancel appointments
 * @param        : none 
 * @inputs       : patientId , appointmentId
 * @constrant    : none
 * @throws       : none
 * @return       : none
 * */


function sendCancelRequest() {
    var json = null;
    var xhr1 = new XMLHttpRequest();
    var url1 = "/cancel_appointment";
    xhr1.open("POST", url1, true);
    xhr1.setRequestHeader("Content-Type", "application/json");

    //todo change patientId
    //var patientId = 1
    var appointmentId = dropdownList.options[dropdownList.selectedIndex].value;

    var data = JSON.stringify({
      //"patient_id": patientId,
        "appointment_id": appointmentId
    });
    xhr1.send(data);
    xhr1.onreadystatechange = function() {
        if (xhr1.readyState === 4 && xhr1.status === 200) {
            json = JSON.parse(xhr1.responseText);
            //todo json.data
            console.log(json)

            if (json['status'] === 'True') {
            console.log("here1");
            alert("Appointment cancelled");
            dropdownList.remove(dropdownList.selectedIndex);
            /*
            var res = json.data;
            modalText.textContent = res;
            modal.style.display = "block";
            setTimeout(function() {
                window.location.href = "./home.html";
            }, 4000);
            */
            } else {
                console.log("here2");
                alert("Couldn't cancel appointment");
            }
            location.reload();
        }
    }
    
}

/*
mockCancelRequest = function() {
    var appointmentId = dropdownList.options[dropdownList.selectedIndex].text;
    modalText.textContent = appointmentId + " has been cancelled. redirecting in 4 seconds...";
    modal.style.display = "block";
    setTimeout(function() {
        window.location.href = "./home.html";
    }, 4000);
}


// When the user clicks the button, open the modal 
btn.onclick = function() {

    sendCancelRequest();
    //            mockCancelRequest();

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
*/