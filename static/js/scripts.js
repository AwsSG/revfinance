$(document).ready(function(){

    /**
     * Add validation for signup form
     */
    $('#signUp').submit( (e) => {
        let errors = []
        const fName = $('#fName')
        const lName = $('#lName')
        const email = $('#email')
        const password = $('#password')
        const checkPassword = $('#checkPassword')
        const errorField = $('#errorMsg')

        if(fName.val() === "" || fName.val() === null) {
            errors.push('Your first name is required.')
        }

        if(lName.val() === "" || lName.val() === null) {
            errors.push('Your last name is required.')
        }

        if(email.val() === "" || email.val() === null) {
            errors.push('Please, enter your email.')
        }

        if(password.val() === "" || password.val() === null) {
            errors.push('Please, enter a password.')
        }

        if(checkPassword.val() === "" || checkPassword.val() === null) {
            errors.push('Please, re-enter your password.')
        }

        if(password.val() != checkPassword.val()) {
            errors.push('Passwords don\'t match')
        }

        if (errors.length > 0) {
            e.preventDefault()
            errorField.html(errors.join('<br>'))
        }
    })

    /**
     * Add validation for new pot form
     */
    $('#createPot').submit( (e) => {

        let errors = []
        const title = $('#title')
        const goal = $('#goal')
        const amount = $('#amount')
        const errorField = $('#errorMsg')

        $('#invited').val(JSON.stringify(inviteList))

        if(title.val() === "" || title.val() === null) {
            errors.push('Please, enter a title for your money pot.')
        }

        if(goal.val() === "" || goal.val() === null) {
            errors.push('Please, enter a goal amount.')
        }

        if(amount.val() === "" || amount.val() === null) {
            errors.push('Please, enter the recurrent payment amount.')
        }

        if (errors.length > 0) {
            e.preventDefault()
            errorField.html(errors.join('<br>'))
        }
    })

 
    $('#addToInvite').attr("disabled", true)

    $('#invite').on('input', () => {

        if($('#invite').val().length == 0) {
            $('#addToInvite').attr("disabled", true)
        } else {
            $('#addToInvite').attr("disabled", false)
        }
    })
    

    inviteList = []

    /* Add list item button */
    $('#addToInvite').click( () => {
        const errorField = $('#errorMsg')
        display = $('.inviteList')
        peerId = 0
        peerEmail = $('#invite').val()
        
        if( validateEmail(peerEmail) && $('#invite').val() != 0) { 
            $('#addToInvite').attr("disabled", false)
            display.append(`<span class="invited" style="display:block">
            <button class="withdrawInvite" type="button" style="padding:0 10px"> X  </button>
            <p style="display:inline">${peerEmail}</p>
            </span>`)
            $('#invite').val('')
            inviteList.push(peerEmail)
        } else {
            errorField.html('Please, enter  avalid email address')
        }
        /* Remove list item button */
        $('.withdrawInvite').on("click", withdrawInvite)
    });

    /* Delete list item */
    function withdrawInvite() {
        remove = $(this).index()
        inviteList.splice(remove, 1);
        $(this).parent().remove();
    }

});

const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

const themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {
    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }
    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
});

// Toggles burger menu 
function myFunction() {
    var x = document.getElementById("myTopNav");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }

  /* Validate email */
function validateEmail(email) {
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    return emailReg.test( email );
    }