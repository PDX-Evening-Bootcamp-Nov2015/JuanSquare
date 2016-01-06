/* function to make GET requests for existing posts
this function will generally run once per page load */
function getPosts() {
  var allPosts; // variable to store array of post objects
  // call on the google spreadsheet to retreive the full list of posts
  $.ajax({
    method: "GET",
    url: "https://spreadsheets.google.com/feeds/list/1_fhQCe0wAmLs0FCOUDn4HZ8eyDq6QHcvQngF7n4e96I/default/public/values?alt=json-in-script",
    dataType: "jsonp"
  }).done(
    function(result){
      alert("Got!"); // development testing item REMOVE ME
      allPosts = result.feed.entry; // store array of posts
      // use array[index].gsx$title.$t to access post titles
      // use array[index].gsx$bodytext.$t to access post contents
    }
  ).fail(
    function(){
      alert("Failed to load forum posts. Sad face.");
    }
  );
  return allPosts;
}

/* function to make POST requests for new posts */
function sendPost() {
  var postTitle = $('#post_title').val(), // pull post title from form
      postText = $('#post_text').val(); // pull post text from form
  // send data to remote google form to get it into the spreadsheet
  $.ajax({
    url: "https://docs.google.com/forms/d/13VwG7osI2qVSGPTw8Dl2LICxUzAi3DwACfkTW5I1ocM/formResponse",
    method: "POST",
    dataType: "xml",
    data: {"entry_1358166143": postTitle, "entry_1289920291": postText}
  }).done(
    // let your friendly neighborhood developer know if it worked
    function(){
      console.log("Post Successful!");
    }
  );
}
