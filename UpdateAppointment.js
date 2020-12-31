window.onload = function getPatientData(appointmentID) {
    $.getJSON('/retrieve_patient_appointments', function (result) {
        var arr = result["data"];
        var el1 = Document.getElementById("name");
        el.textContent = arr["patient_name"];
        var
        var el2 = Document.getElementById("age");
        el.textContent = arr["patient_age"];
        var el3 = Document.getElementById("email");
        el.textContent = arr["patient_email"];
        var el4 = Document.getElementById("patientNumber");
        el.textContent = arr["patient_phone_number"];
    });
}

function getIllness() {
    $.getJSON("/specialization", function (result) {
        var arr = result["data"];
        var select = document.getElementById("illness")
        for (var i = 0; i < arr.length; i++) {
            var spec = arr[i];
            var el = document.createElement("option");
            el.textContent = spec;
            el.value = spec;
            select.appendChild(el);
        }
    });
}

function getDoctors(illnessSpecification) {
    $.getJSON('/doctors', {
        specialization: illnessSpecification
    }, function (result) {
        var arr = result["data"];
        if (arr !== "none" && arr.length) {
            var select = document.getElementById("Doctors")
            for (var i = 0; i < arr.length; i++) {
                var spec = arr[i];
                var el = document.createElement("option");
                el.textContent = "ID: " + spec["id"] + " - name: " + spec["name"] + " - specialization: " + spec["specialization"];
                el.value = spec;
                select.appendChild(el);
            }
        }
    });
}

function getDate(DrDate) {
    $.getJSON('/dr_appointments', {
        doctors: DrDate
    }, function (result) {
        var arr = result["data"];
        if (arr !== "none" && arr.length) {
            var select = document.getElementById("Times")
            for (var i = 0; i < arr.length; i++) {
                var dr = arr[i];
                var el = document.createElement("option");
                el.textContent = "ID: " + dr["id"] + " - name: " + dr["name"] + " - doctors: " + dr["doctors"];
                el.value = dr;
                select.appendChild(el);
            }
        }
    });
}

 function option(op, DrDate) {
        if (op.value == 0) {
            getDate(DrDate);
            document.getElementById('times').readOnly = true;
        } else if (op == 1) {
            getDate(DrDate);
            document.getElementById('doctors').readOnly = true;
        }
     
var form = document.getElementsByClassName("form-1")[0];

function handleForm(event) {
    event.preventDefault();
}
form.addEventListener("submit", handleForm);
     
        window.onload = function() {
            var patientId = "1";
            mockGetAppointments();
        };
     

/* *
 * @brief         : sends post request to update appointment
 * @param         : none 
 * @inputs        : appointmentId
 * @constraint    : none
 * @throws        : none
 * @return        : none
 * */


sendUpdateRequest = function () {
    var xhr1 = new XMLHttpRequest();
    var url1 = "/update_appointment";
    xhr1.open("POST", url1, true);
    xhr1.setRequestHeader("Content-Type", "application/json");
    xhr1.onreadystatechange = function () {
        if (xhr1.readyState === 4 && xhr1.status === 200) {
            var json = JSON.parse(xhr1.responseText);
            //todo json.data
            if (json.data != 'none') {
                var res = json.data;
                if(res == 'true'){
                modalText.textContent = "Your appointment" + appointmentId + " has been updated. redirecting to home page...";
                modal.style.display = "block";
                setTimeout(function () {
                    window.location.href = "./home.html";
                }, 4000);}
                else if(res == 'false'){
                modalText.textContent = "Your appointment" + appointmentId + "Is not updated. redirecting to your appointments...";
                modal.style.display = "block";
                setTimeout(function () {
                    window.location.href = "../Appointments.html";
                }, 4000);}
                }
            }
        }
    }

    }

    var op = 0;
    var oldAppointmentId = dropdownList.options[dropdownList.selectedIndex].text;
    var newAppointmentId = 1;

    var data = JSON.stringify({
        "appointment_id": appointmentId
    });

    xhr1.send(data);

}

function submitFun() {

    alert("submit");

}

makeUpdateRequest = function() {
            var appointmentId = dropdownList.options[dropdownList.selectedIndex].text;
            modalText.textContent = appointmentId + " has been updated. redirecting to home page...";
            modal.style.display = "block";
            setTimeout(function() {
                window.location.href = "./home.html";
            }, 4000);
        }


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("submit");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var modalText = document.getElementById("modaltext");

// When the user clicks the button, open the modal 
btn.onclick = function () {
     makeUpdateRequest();

}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
