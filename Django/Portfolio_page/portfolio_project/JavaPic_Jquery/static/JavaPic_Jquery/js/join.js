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

/* function to check if field is required
    - takes a jQuery object as an input
    - returns true if element is required */
function isRequired(field) {
  return !(!field.attr('required'));
}

/* function to check if field has a value
    - takes a jQuery object as an input
    - returns true if field is empty */
function isEmpty(field) {
  return !field.val();
}

/* function to check if e-mail field has a correctly formatted e-mail */
function isEmail(field) {
  var mailRegEx = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  return mailRegEx.test(field.val());
}

/* function to create and return error messages */
function errMessage(err) {
  // object to store error messages
  var messages = {
    reqField: "This field is required.",
    notEmail: "Please enter a valid e-mail address."
  };
  // return appropriate error messages
  return messages[err];
}

/* function to remove previous error styling */
function unstyleErrors() {
  var $errMessages = $('.error'), // select created error messages
      $inputs = $('input'); // select all input fields
  $inputs.css('outline', 'none'); // remove nasty red borders
  $errMessages.remove(); // done with error messages
}

/* function to add error styling
    - field is a jQuery object referencing the field with an error
    - error is a string referencing the type of error */
function styleError($field, err) {
  // create error message
  var $errorDiv = $('<div>');
  $errorDiv.css({
    'color': 'red',
    'font-size': '0.8rem',
  }).addClass('error')
  .text(errMessage(err));
  // add error div to DOM after field
  $field.after($errorDiv);
  // style the field with a red border
  $field.css('outline', '1px solid red');
}


/* function to call all validation functions
and decide if form submit passes */
function validateAll(event) {
  var $fields = $('input'), // select all inputs
      $form = $('#signup'), // select whole form
      errorCount = 0;
  unstyleErrors(); // remove previous error styling
  // check each input field
  $fields.each(function(index, field) {
    var $currField = $(field), // convert element to jQuery object
        fieldType = $currField.attr('type');
    if (fieldType === 'email' && !isEmail($currField)) {
      styleError($currField, 'notEmail');
      errorCount++;
    } else if (isRequired($currField) && isEmpty($currField)) {
      styleError($currField, 'reqField');
      errorCount++;
    }
  });
  // pass along username to next page if no validation issues
  if (!errorCount) {
    var username = $('input[name=username]').val(); // retreive username
    $form.attr('action', 'gallery.html?username=' + username);
  } else {
    event.preventDefault(); // prevent page reload if validation errors
  }
}


// on pageload stuff
$('document').ready(function(){
  $('#signup').attr('noValidate', '');
  $('#submit').click(validateAll);
});
