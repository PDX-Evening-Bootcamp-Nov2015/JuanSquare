/*
Requirements
_gallery.html_
  - update the slogan to add a ", user_name", with the user's name
  - loop through the image folder and display each image in the folder
  - add the functionality so that if a user clicks on an image, the lightbox
  appears with that image loaded in
  - when the lightbox is up, is the user clicks anywhere not on the image, the
  lightbox closes
*/

/* function to generate image path
    NOTE: this function assumes files follow a naming convention with
    two-digit, zero-padded integers */
function imgPath(imgNum){
  imgNum = String(imgNum);
  // check if image number needs zero padding
  if (imgNum.length < 2) {
    imgNum = '0' + imgNum;
  }
  // add properly padded number to path and return
  return 'images/pdxcg_' + imgNum + '.jpg';
}

/* function to generate new li containing image */
function genImg(imgNum){
  var $newLi = $('<li>');
      $newImg = $('<img>');
  $newImg.attr({
    'src': imgPath(imgNum), // add correct url
    'alt': 'Image not Found. Sorry!'
  }).error(function(){
    // give the user a kitten if you can't find an image
    $(this).attr('src', 'http://placekitten.com/g/500/500')
  });
  $newLi.append($newImg); // li wrapper needed for styling
  return $newLi;
}

/* function to get number of images */
function getNumImgs() {
  var i = 1, // counter variable for do while
      imgFound = false; // stop condition for image count
  do {
    // check at least once for images
    var url = imgPath(i);
    $.ajax({
      // ajax call checks if an image exists with each path
      url : url,
      success : function(){
        imgFound = true;
        i += 1;
      },
      error : function(){
        imgFound = false;
        if (i === 1) {
          i = 60; // sets a default number of images if no ajax calls succeed
        }
      }
    })
  } while (imgFound) // stop when no more images found
  return i;
}

/* function to populate gallery */
function popGallery(numImgs) {
  for (var i = 1; i <= numImgs; i++) {
    $('#gallery').append(genImg(i));
  }
}

/* function to parse username from url */
function getUserName() {
  // check the url and store it in a variable so we can search it
  var url = $(location).attr('href'),
      urlComponents,
      username;
  // split the url into searchable components
  urlComponents = url.split('?')
  // search the match data for the passed username and return it
  for (var i = 0; i < urlComponents.length; i++){
      // split the string again to compare value pairs
      compComponents = urlComponents[i].split('=');
      if (compComponents[0] === 'username') {
        return compComponents[1];
      }
  }
}

/* function to insert the username into the page */
function popUName(uName) {
  var $tagline = $('.tagline');
      spanText = $tagline.text(); // cache tagline text
  spanText += ', ' + uName;
  $tagline.text(spanText);
}

/* function to select clicked image and display in lightbox */
function imgClick(event) {
  var clickTargetPath = $(event.target).attr('src'), // find the click target
      $lightbox = $('#image_show'),
      $boxImage = $('#image_show img');
  // check to see if lightbox is already displayed
  if ($lightbox.hasClass('display_img')) {
      closeLightbox();
      return
  }
  // attach a click listener for closing the lightbox
  $(window).click(closeLightbox);
  $boxImage.click(function(evt){
    evt.stopPropagation() // ignore clicks on the lightbox image
  })
  // change lightbox image targete
  $boxImage.attr('src', clickTargetPath);
  // display the lightbox
  $lightbox.addClass('display_img').removeClass('display_none');
}

/* function to close lightbox on a click elsewhere
    - imgClick function has already bound a stopPropagation
    to keep clicks on the lightbox itself from registering */
function closeLightbox(event) {
  var $lightbox = $('#image_show'),
      $boxImage = $('#image_show img');
  event.preventDefault(); // don't want to follow any links by accident
  // unbind stopPropagation to prevent side effects
  $boxImage.off('click');
  // unbind click listener to prevent listener clutter
  $(window).off('click');
  // hide the lightbox
  $lightbox.addClass('display_none').removeClass('display_img');
}

$(function(){
  /* page load functions:
      - populate username
      - populate images
      - attach event listeners to images */
  var userName = getUserName(),
      numImgs = getNumImgs();
  popUName(userName);
  popGallery(numImgs);
  $('#gallery').on('click', 'img', imgClick);
})
