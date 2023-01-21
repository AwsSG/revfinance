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

});
