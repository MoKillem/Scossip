function checkFirstName() {
    var value1 =  document.getElementById("FirstName");
    sm1 = document.getElementById("sm1");
    if (value1.value.length == 0) {
        sm1.innerHTML = "Please enter your first name!";
        sm1.style.color = "white";
        sm1.style.background = "red";
        value1.style = "border-color: #d9534f";
        } else{
        sm1.innerHTML = "";
        sm1.style.color = "white";
        sm1.style.background = "white";
        value1.style = "border-color: #d0d0e1";
        }
    }


function checkLastName() {
    var value2 =  document.getElementById("LastName");
    sm2 = document.getElementById("sm2");
    if (value2.value.length == 0) {
       sm2.innerHTML = "Please enter your last name!";
        sm2.style.color = "white";
        sm2.style.background = "red";
        value2.style = "border-color: #d9534f";
    } else {
        sm2.innerHTML = "";
        sm2.style.color = "white";
        sm2.style.background = "white";
        value2.style = "border-color: #d0d0e1";
    }
}

function checkEmail() {
    var email = document.getElementById("Email");
    var patt = new RegExp("^(.+)@([a-zA-Z0-9]+)\.(com|COM)$");
    sm4 = document.getElementById("sm4");
    if (!patt.test(email.value)) {
        sm4.innerHTML = "Please enter you email in the correct form!";
        sm4.style.color = "white";
        sm4.style.background = "red";
        email.style = "border-color: #d9534f";
        } else {
        sm4.innerHTML = "";
        sm4.style.color = "white";
        sm4.style.background = "white";
        email.style = "border-color: #d0d0e1";
        }
}

function checkUserName() {
    var userName = document.getElementById("UserName");
    var patt = new RegExp("^([a-zA-Z0-9]{6,20})$");
    sm3 = document.getElementById("sm3");
    if (!patt.test(userName.value)) {
        sm3.style.color = "white";
        sm3.style.background = "red";
        userName.style = "border-color: #d9534f";
       } else {
        sm3.style.color = "red";
        sm3.style.background = "white";
        userName.style = "border-color: #d0d0e1";
       }
}

function checkPassword() {
    var password = document.getElementById("Password");
    var patt = new RegExp("^([a-zA-Z0-9]{8,20})$");
    if (!patt.test(password.value)) {
        sm = document.getElementById("sm5");
        sm.style.color = "white";
        sm.style.background = "red";
        password.style = "border-color: #d9534f";
        } else{
        sm.style.color = "red";
        sm.style.background = "white";
        password.style = "border-color: #d0d0e1";
        }
}


function checkConpass() {
    var ConPass = document.getElementById("ConfirmPassword");
    var password = document.getElementById("Password");
    sm6 = document.getElementById("sm6");
    if (ConPass.value != password.value) {
        sm6.innerHTML = "Please enter the same password!";
        sm6.style.color = "white";
        sm6.style.background = "red";
        ConPass.style = "border-color: #d9534f";
        } else {
        sm6.innerHTML = "";
        sm6.style.color = "white";
        sm6.style.background = "white";
        ConPass.style = "border-color: #d0d0e1";
        }
}

function checkCampus() {
    var campus = document.getElementById("sell");
    sm8 = document.getElementById("sm8");
    if (campus.value.length == 0 ) {
        sm8.innerHTML = "Please select your campus!";
        sm8.style.color = "white";
        sm8.style.background = "red";
        campus.style = "border-color: #d9534f";
        } else {
        sm8.innerHTML = "";
        sm8.style.color = "white";
        sm8.style.background = "white";
        campus.style = "border-color: #d0d0e1";
        }
}

function checkAge() {
    var age = document.getElementById("Age");
    sm7 = document.getElementById("sm7");
    if (age.value.length ==0 ) {
        sm7.innerHTML = "Please enter your age!";
        sm7.style.color = "white";
        sm7.style.background = "red";
        age.style = "border-color: #d9534f";
        } else {
        sm7.innerHTML = "";
        sm7.style.color = "white";
        sm7.style.background = "white";
        age.style = "border-color: #d0d0e1";
        }
}


function checkAll() {
    var campus = document.getElementById("sell").value;
    var value1 =  document.getElementById("FirstName").value;
    var value2 =  document.getElementById("LastName").value;
    var email = document.getElementById("Email").value;
    var age = document.getElementById("Age").value;
    var ConPass = document.getElementById("ConfirmPassword").value;
    var password = document.getElementById("Password").value;
    if (age.length ==0 || campus.length == 0 || value1.length == 0 || value2.length == 0 || email.length == 0 || ConPass.length == 0 || password.length == 0) {
        window.alert("Please make sure you fill in all of the blanks!");
        }
    if (email.length != 0) {
        checkEmail();
        }
    if (password.length != 0) {
        checkPassword();
        }
    if (ConPass!= 0) {
        checkConpass();
        }
}