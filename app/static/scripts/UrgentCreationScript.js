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

function urgentCreate() {
    event.preventDefault();

    var specialization = $("#illness-spec :selected").val();
    var firstName = $("#first-name").val();
    var lastName = $("#last-name").val();
    var age = $("#patient-age").val();
    var email = $("#email").val();
    var number = $("#patient-number").val();

    var fullName = firstName + " " + lastName;
    
    var requestParams = {'patient_name' : fullName,
                        'patient_age' : age,
                        'patient_email' : email,
                        'patient_phone_number' : number,
                        'specialization' : specialization};
    console.log("here")
    console.log(requestParams);

    $.post('/urgent_appointment', requestParams, function(response) {
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