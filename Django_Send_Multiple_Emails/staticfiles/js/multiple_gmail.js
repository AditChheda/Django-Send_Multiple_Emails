function Upload() {
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var cells = rows[i].split(",");
                    if (cells.length > 1) {
                        var row = table.insertRow(-1);
                        for (var j = 0; j < cells.length; j++) {
                            var cell = row.insertCell(-1);
                            cell.innerHTML = cells[j];
                        }
                    }
                }
                var dvCSV = document.getElementById("dvCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);
            }
            reader.readAsText(fileUpload.files[0]);
        } else {
            fileUpload.value = '';
            alert("This browser does not support HTML5.");
        }
    } else {
        fileUpload.value = '';
        div_visible.style.visibility = "hidden";
        alert("Please upload a valid CSV file.");
    }
}

function SearchEmailSuccess(){
    var input_search = document.getElementById('search_email_success').value.toUpperCase();
    var div_email_success = document.getElementsByClassName('div_email_success');
    var div_success = document.getElementsByClassName('div_success');
    for(i = 0; i < div_email_success.length; i++){
        var div_email_name = div_email_success[i].innerText.toUpperCase();
        if(div_email_name.indexOf(input_search)>-1){
            div_success[i].style.display = "";
        }else{
            div_success[i].style.display = "none";
        }
    }
}

function SearchEmailFailure(){
    var input_search = document.getElementById('search_email_failure').value.toUpperCase();
    var div_email_failure = document.getElementsByClassName('div_email_failure');
    var div_failure = document.getElementsByClassName('div_failure');
    for(i = 0; i < div_email_failure.length; i++){
        var div_email_name = div_email_failure[i].innerText.toUpperCase();
        if(div_email_name.indexOf(input_search)>-1){
            div_failure[i].style.display = "";
        }else{
            div_failure[i].style.display = "none";
        }
    }
}