window.onload = function getIllness() {
    $.getJSON("/specialization", function(result) {
        var arr = result["data"];
        console.log(arr);
        var select = document.getElementById("illness-spec");
        for (var i = 0; i < arr.length; i++) {
            var spec = arr[i];
            var el = document.createElement("option");
            el.textContent = spec;
            el.value = spec;
            select.appendChild(el);
        }
    });
}

$('#illness-spec').on('change', function() {
    $('#Doctors-Name').empty().append('<option value="" selected>Choose a doctor</option>');
    var specialization = $("#illness-spec :selected").val();
    if(specialization.valueOf().trim() !== "") {
        $.getJSON('/doctors', {'option': 0, 'specialization' : specialization}, function(result){
            var arr = result["data"];
            console.log(arr);
            if(arr !== "none" && arr.length) { 
                var select = document.getElementById("Doctors-Name")
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
});

$('#Doctors-Name').on('change',function() {
    $('#Date-time').empty().append('<option value="" selected>Choose an appointment</option>');
    var doctorID = $("#Doctors-Name :selected").val();
    if(doctorID.valueOf().trim() !== "") {
        $.getJSON('/dr_appointments', {option: 0, dr_id: doctorID}, function(result){
            var arr = result['data'];
            console.log(arr);
            if(arr !== "none" && arr.length) {
                var select = document.getElementById("Date-time");
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
});

function bookNormalAppointment() {
    event.preventDefault();
    var specialization = $("#illness-spec :selected").val();
    var appointment_id = $("#Date-time :selected").val();
    console.log(appointment_id);
    var firstName = $("#first-name").val();
    var lastName = $("#last-name").val();
    var age = $("#patient-age").val();
    var email = $("#email").val();
    console.log('email: ' + email);
    var number = $("#patient-number").val();
    //var gender = document.getElementsByName("gender").value;
    var fullName = firstName + " " + lastName;
    console.log(fullName);
    
    var requestParams = {'appointment_id' : appointment_id,
                        'patient_name' : fullName,
                        'patient_age' : age,
                        'patient_email' : email,
                        'patient_phone_number' : number,
                        'specialization' : specialization};

    $.post('/normal_appointment', requestParams, function(response) {
        var status = response['status'];
        console.log(status);
        if(status === 'True') {
            alert("Appointment booked");
        } else {
            alert("Couldn't book appointment");
        }
        location.reload();
    });
}