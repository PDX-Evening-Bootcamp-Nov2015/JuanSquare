// this script will cover form validation, and will also disable default form
// validation to ensure cross broswer experience is the same
/*Requirements:
- _join.html_
  - add form validation that works in all major browsers (you'll need to
  deactivate browser validate to check this)
  - form validation should have all fields marked "required" required, and all
  email fields should require and check for proper email syntax.
  - any validation errors should be presented clearly to the user so that they
  may correct them
  - on completion of the form, navigate the user to the gallery, passing their
  name to the page
*/

// function to check if field is required
function isRequired(field) {
  return field.hasAttribute('required') || (typeof field.required === 'string');
}

// function to check if field has a value
function noValue(field) {
  return !field.value || field.value === field.placeholder;
}

// function to check if e-mail field has a correctly formatted e-mail
function isEmail(field) {
  var mailRegEx = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  return mailRegEx.test(field.value);
}

// function to create and return error messages
function errMessage(err) {
  // object to store error messages
  var messages = {
    reqField: "This field is required.",
    eField: "Please enter a valid e-mail address."
  };
  // return appropriate error messages
  return messages[err];
}

// function to remove previous error styling
function unstyleErrors() {
  // find any existing error text on the page
  var errMessages = document.getElementsByClassName('error'),
      form = document.getElementById('signup'),
      i, loop = errMessages.length;
  // get rid of them nasty red borders
  for (i = 0; i < form.length; i++) {
    form[i].style.outline = '';
  }
  // remove all existing error text
  for (i = loop - 1; i >= 0; i--) {
    errMessages[i].parentNode.removeChild(errMessages[i]);
  }
}

// function to add error styling
function styleError(field, err) {
  // creating error message div and making it purdy
  var errorDiv = document.createElement('div');
  errorDiv.style.color = 'red';
  errorDiv.style.fontSize = '0.8rem';
  errorDiv.classList.add('error');
  // retrieve and attach appropriate error message
  errorDiv.innerText = errMessage(err);
  // OMG LOOK AT THAT FIELD (it's red now)
  field.style.outline = '1px solid red';
  // add error message after field
  field.parentNode.insertBefore(errorDiv, field.nextSibling);
}

// function to call all validation functions and decide if form submit passes
function validateAll(event) {
  // retrieve all form fields
  var formFields = document.forms.signup,
      username,
      errors = 0;
  // remove previous error styling
  unstyleErrors();
  // loop through the array of form fields
  for (i = 0; i < formFields.length - 1; i++) {
    var curr = formFields[i];
    if (isRequired(curr) && noValue(curr)) {
      // check if field is required and empty
      event.preventDefault();
      styleError(curr, 'reqField');
      errors++;
    } else if (curr.type === 'email' && !isEmail(curr)) {
      // check if field is an e-mail field
      event.preventDefault();
      styleError(curr, 'eField');
      errors++;
    }
  }
  // if all is valid pass the username on to the next page
  if (!errors) {
    username = formFields.username.value;
    formFields.action = 'gallery.html?username=' + username;
  }
}

// on pageload
window.onload = function () {
  var form = document.forms.signup;
  // disable form validation
  form.setAttribute('noValidate', '');
  // event listener to validate form
  form.submit.addEventListener('click', validateAll, false);
};
