const signInBtnLink = document.querySelector('.signInBtn-link');
const signUpBtnLink = document.querySelector('.signUpBtn-link');
const wrapper = document.querySelector('.wrapper');
let password1=document.querySelector('.signInPassword');
let password2=document.querySelector('.signUpPassword');
signUpBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
});
signInBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
});

function fun1(t){
    t.classList.toggle('fa-eye');
    if(password1.type=='password'){
        password1.type='text';
    }
    else{
        password1.type='password'
    }
}
function fun2(t){
    t.classList.toggle('fa-eye');
    if(password2.type=='password'){
        password2.type='text';
    }
    else{
        password2.type='password'
    }
}