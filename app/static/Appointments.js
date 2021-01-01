        // Get appointments request
        window.onload = function () {
            //todo patientId?
            var patientId = "1";
            mockGetAppointments();
        };

        var dropdownList = document.getElementById("appointment-num");


        mockGetAppointments = function () {
            var opt = document.createElement('option');

            opt.appendChild(document.createTextNode('Appointment 1'));
            opt.value = 'Appointment 1';
            dropdownList.appendChild(opt);
        }

        /* *
         * @brief        : sends post request to get appointments
         * @param        : patientId
         * @constrant    : none
         * @throws       : none
         * @return       : none
         * */

        getAppointments = function (patientId) {
            var xhr = new XMLHttpRequest();
            var url = "/retrive_patient_appointment";
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    if (json.data != 'none') {
                        var appendData = "";
                        for (var i in json.data) {
                            var opt = document.createElement('option');
                            opt.appendChild(document.createTextNode(json.data[i].appointment_id));
                            opt.value = json.data[i].appointment_id;
                            dropdownList.appendChild(opt);
                        }
                    }
                }
            };

            var data = JSON.stringify({
                "patient_id": patientId
            });
            xhr.send(data);
        }
