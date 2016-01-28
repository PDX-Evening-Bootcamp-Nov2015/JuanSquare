/*
This is a single page forum application.
This application uses a google spreadsheet as a database,
and calls to a google form to make posts.
Required functionality:
 - get posts
 - send posts
 - display posts
*/

/* function to populate page with posts */
function populate(allPosts) {
  // use allPosts[index].gsx$title.$t to access post titles
  // use allPosts[index].gsx$bodytext.$t to access post contents
  var $postArea = $('#post_display'), // div that contains all posts
      totalPosts = allPosts.length;
  $postArea.html(''); // clear old posts for refresh
  for (var i = 0; i < totalPosts; i++) {
    var postTitle = allPosts[i].gsx$title.$t, // cache post title
        postText = allPosts[i].gsx$bodytext.$t, // cache post body
        attributes = {'id': i, 'class': 'post'},
        $newDiv = $('<div>').attr(attributes); // create new div for post
    $newDiv.append($('<h3>').html(postTitle)); // populate new div with title
    $newDiv.append($('<p>').html(postText)); // populate new div with body text
    $postArea.prepend($newDiv); // add completed post to the page
  }
}

/* function to make GET requests for existing posts
this function will run at page load and each time a new post is made*/
function getPosts() {
  var allPosts; // variable to store array of post objects
  // call on the google spreadsheet to retreive the full list of posts
  $.ajax({
    method: "GET",
    url: "https://spreadsheets.google.com/feeds/list/1_fhQCe0wAmLs0FCOUDn4HZ8eyDq6QHcvQngF7n4e96I/default/public/values?alt=json-in-script",
    dataType: "jsonp"
  }).done(
    function(result){
      allPosts = result.feed.entry; // store array of posts
      // use allPosts[index].gsx$title.$t to access post titles
      // use allPosts[index].gsx$bodytext.$t to access post contents
      populate(allPosts);
    }
  ).fail(
    function(){
      alert("Failed to load forum posts. Sad face.");
    }
  );
}

/* function to make POST requests for new posts */
function sendPost(postTitle, postText) {
  var updatedPosts;
  // send data to remote google form to get it into the spreadsheet
  $.ajax({
    url: "https://docs.google.com/forms/d/13VwG7osI2qVSGPTw8Dl2LICxUzAi3DwACfkTW5I1ocM/formResponse",
    method: "POST",
    dataType: "xml",
    data: {"entry_1358166143": postTitle, "entry_1289920291": postText}
  }).always(function(){
    getPosts(); // reload posts to display new one
  });
}

/* function to handle form clicks */
function formSubmit(evt) {
  // cache field references
  var $postTitle = $('#post_title'),
      $postText = $('#post_text');
  evt.preventDefault(); // stop page reload
  sendPost($postTitle.val(), $postText.val()); // send AJAX to google form and update page
  // clear old values from fields
  $postTitle.val('');
  $postText.val('');
}

/* display or hide new post form */
function showForm(evt) {
  if($('.new_post').hasClass('no_height')) {
    $('.new_post').removeClass('no_height');
  } else {
    $('.new_post').addClass('no_height');
  }
}


/* page load functions */
$(function(){
  var $postButton = $('#make_post'),
      $formRevealButton = $('#form_reveal');
  getPosts(); // pull existing posts and populate page
  $postButton.click(formSubmit); // tie to form submission actions
  $formRevealButton.click(showForm);
});
