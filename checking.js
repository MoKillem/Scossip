function checkFirstName() {
    var value1 =  document.getElementById("FirstName").value;
    if (value1.length === 0) {
        window.alert("Please enter your first name!");
    }
}

function checkLastName() {
    var value2 =  document.getElementById("LastName").value;
    if (value2.length === 0) {
        window.alert("Please enter your last name!");
    }
}

function checkEmail() {
    var email = document.getElementById("Email").value;
    var patt = new RegExp("^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.(com|COM)$");
    if (!patt.test(email)) {
        window.alert("Please enter your email address in the correct form!");
        }
}

function checkUserName() {
    var userName = document.getElementById("UserName").value;
    var patt = new RegExp("^([a-zA-Z0-9]{6,20})$");
    if (!patt.test(userName)) {
       window.alert("Please enter the user name in the correct form! -- 6-20 digits with only letters and numbers");
       }
}

function checkPassword() {
    var password = document.getElementById("Password").value;
    var patt = new RegExp("^([a-zA-Z0-9]{8,20})$");
    if (!patt.test(password)) {
        window.alert("Please make sure your password is between 8-20 digits long and have no elements other than letters and numbers!");
        }
}


function checkConpass() {
    var ConPass = document.getElementById("ConfirmPassword").value;
    var password = document.getElementById("Password").value;
    if (ConPass != password) {
        window.alert("Please make sure you entered the same passwords!");
        }
}

function checkCampus() {
    var campus = document.getElementById("sell").value;
    if (campus.length ==0 ) {
        window.alert("Please select your campus!");
        }
}

function checkAge() {
    var age = document.getElementById("Age").value;
    if (age.length ==0 ) {
        window.alert("Please enter your age!");
        }
}

function checkDes() {
    
}