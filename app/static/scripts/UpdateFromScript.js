var dropdownList = document.getElementById("appointment-num");
var checkbox = document.getElementById('change-doctor-check');
var drDropDownList = document.getElementById("Doctors-Name");
var otherDatesList = document.getElementById("other-dates");
var initialDrID = null;
var currDrID = null;
var appointment_id = null;
var appointmentsDict = {};

function popDict(appointments) {
    //console.log(appointments);
    for(var i = 0; i < appointments.length; ++i) {
        appointment = appointments[i];
        appointmentsDict[appointment["appointment_id"]] = appointment;
        //console.log(appointmentsDict[appointment["appointment_id"]])
    }
}

window.onload = function(patientId) {
    checkbox.disabled = true;
    drDropDownList.disabled = true;

    var xhr = new XMLHttpRequest();
    var url = "/retrieve_patient_normal_appointments";

    xhr.open("GET", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            json = json['data'];
            if (json != 'none') {
                var appoint = "";
                for (var i = 0; i < json.length; ++i) {
                    console.log(appoint);
                    appoint = json[i];
                    var opt = document.createElement('option');
                    opt.textContent = 'appointment id: ' + appoint['appointment_id'] + " - patient's name: " + appoint['patient_name'] + " - dr's spec: " + appoint['specialization'];
                    opt.value = appoint['appointment_id'];
                    dropdownList.appendChild(opt);
                }
                popDict(json);
            }
        }
    };
    var data = JSON.stringify({
        //"patient_id": patientId
    });
    xhr.send(data);
}

function fillAppointmentInfo(appointment_id) {
    var appointment = appointmentsDict[appointment_id];
    console.log(appointment)
    document.getElementById("a-id").innerHTML = appointment['appointment_id'];
    document.getElementById("a-spec").innerHTML = appointment['specialization'];
    document.getElementById("p-id").innerHTML = appointment['patient_id'];
    document.getElementById("p-name").innerHTML = appointment['patient_name'];
    document.getElementById("p-age").innerHTML = appointment['patient_age'];
    document.getElementById("p-email").innerHTML = appointment['patient_email'];
    document.getElementById("p-number").innerHTML = appointment['patient_phone_number'];
}

function clearAppointmentInfo() {
    document.getElementById("a-id").innerHTML = "";
    document.getElementById("a-spec").innerHTML = "";
    document.getElementById("p-id").innerHTML = "";
    document.getElementById("p-name").innerHTML = "";
    document.getElementById("p-age").innerHTML = "";
    document.getElementById("p-email").innerHTML = "";
    document.getElementById("p-number").innerHTML = "";
}

initAltDates = $('#appointment-num').on('change', function() {
    appointment_id = $("#appointment-num :selected").val();
    $('#other-dates').empty().append('<option value="" selected>Choose an appointment</option>');
    if(appointment_id.trim() !== "") {
        var url = "/dr_by_appointment_id";
        var req_params = {'appointment_id' : appointment_id};
        $.getJSON(url, req_params, function(result) {
            var dr_id = result['data'];
            if(dr_id !== "none") {
                initialDrID = dr_id;
                initDrsDates();
                fillAppointmentInfo(appointment_id);
            }
            checkbox.disabled = false;
        });
    } else {
            checkbox.disabled = true;
            clearAppointmentInfo();
    }
});

function initDrsDates() {
    if(checkbox.checked == true) {
        console.log("checked");
        drDropDownList.disabled = false;
        getDoctors();
    } else {
        console.log("not checked");
        drDropDownList.disabled = true;
        // get appointments of the initial dr
        getDrDates(appointment_id, null);
    }
}

$("#change-doctor-check").on("change", function() {
    initDrsDates();    
});

// get doctors of the same specialization
getDoctors = function() {
    if(checkbox.checked) {
        $('#Doctors-Name').empty().append('<option value="" selected>Choose an appointment</option>');
        //console.log(checkbox.enabled);
        appointment_id = $("#appointment-num :selected").val();
        if(appointment_id.trim() !== "") {
            var reqParams = {"option": 1, "appointment_id": appointment_id};
            $.getJSON('/doctors', reqParams, function(result) {
                var arr = result["data"];
                console.log(arr);

                if(arr !== "none" && arr.length) { 
                    var select = document.getElementById("Doctors-Name");
                    for(var i = 0; i < arr.length; i++) {
                        var doctor = arr[i];
                        var el = document.createElement("option");
                        el.textContent = "ID: " + doctor["id"] + " - name: " + doctor["name"];
                        el.value = doctor["id"];
                        select.appendChild(el);
                    }
                }
            });
        }
    }
}

function getDrDates(appointment_id, dr_id) {
    $('#other-dates').empty().append('<option value="" selected>Choose an appointment</option>');
    //var dr_id = $("#Doctors-Name :selected").val();
    if(appointment_id !== "") {
        var reqParams = null;
        if(dr_id === null) {
            reqParams = {"option" : 1, "appointment_id": appointment_id};
        } else {
            reqParams = {"option" : 0, "dr_id": dr_id};
        }
        $.getJSON('/dr_appointments', reqParams, function(result) {
            var arr = result["data"];
            console.log(arr);
            if(arr !== "none" && arr.length) { 
                var select = otherDatesList;
                for(var i = 0; i < arr.length; i++) {
                    var appointment = arr[i];
                    var el = document.createElement("option");

                    el.textContent = "ID: " + appointment["appointment_id"] + " - start date: " + appointment["start_date"] + " - end date: " + appointment["end_date"];
                    el.value = appointment["appointment_id"];
                    select.appendChild(el);
                }
            }
        });
    }
};

getOtherDrDates = $('#Doctors-Name').on('change', function() {
    console.log("here");
    var dr_id = $("#Doctors-Name :selected").val();
    console.log(dr_id)
    if(dr_id !== "") {
        getDrDates(appointment_id, dr_id);
    }
});

function updateAppointment() {
    event.preventDefault();
    console.log('inside update');
    var new_appointment_id = $("#other-dates :selected").val();
    console.log(new_appointment_id);
    if(new_appointment_id !== null || new_appointment_id !== "") {
        var url = "/update_appointment";
        var req_params = {"old_appointment_id" : appointment_id,
                            "new_appointment_id": new_appointment_id};
        $.post(url, req_params, function(response) {
            var status = response['status'];
            if(status === "True") {
                alert("appointment updated");
            } else {
                alert("appointment couldn't be updated");
            }
            location.reload();
        });
    }
}