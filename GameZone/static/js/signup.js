let alertElement = document.getElementById("alertElement")
let text = document.querySelector(".text")
// let formEl = document.forms.signupForm;
let formEl = document.getElementById("signupForm").elements;

let pat1 = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
let pat2 = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/

let demo = document.querySelector(".demo")

// console.log(demo)

// demo.innerHTML = ''
let cnt = 0

let email = formEl['email']
let pass = formEl['password']
let pass1 = formEl['confirm_password']

function checkFormData() {
    if(cnt > 0){
        console.log(cnt)
        // demo.innerHTML = ""
        // demo.innerHTML = '<div id="alertElement" class="alert alert-success alert-dismissible"> <button type="button" class="btn-close" data-bs-dismiss="alert"></button> <p class="text" > <strong>Success!</strong> This alert box could indicate a successful or positive action.</p></div > '
    }
    
    if (!(pat1.test(email.value))) {
        console.log(email.value)
        console.log(alertElement)
        
        demo.classList.remove("d-none")
        alertElement.classList.remove("alert-success")
        alertElement.classList.add("alert-danger")
        cnt++


        text.innerHTML = "<strong>Please</strong> enter valid email !!"

        return false    
    }
    else if (!(pat2.test(pass.value))) {
        console.log(pass.value)
        console.log(alertElement)
        console.log(alertElement.classList)

        demo.classList.remove("d-none")
        alertElement.classList.remove("alert-success")
        alertElement.classList.add("alert-danger")
        cnt++

        text.innerHTML = "<strong>Please</strong> enter strong password!!"

        return false
    }
    else if (pass.value !== pass1.value) {
        demo.classList.remove("d-none")
        alertElement.classList.remove("alert-success")
        alertElement.classList.add("alert-danger")
        cnt++

        text.innerHTML = "<strong>Please</strong> your password and confirm password are not same!!"

        return false
    }

}

