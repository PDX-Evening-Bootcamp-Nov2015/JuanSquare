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

// function to check if image is in the images folder
function imgExists(imgNum, numImgs) {
  var missImgs = [42]; // list of images numbers missing from the images folder
  // check if image number is on the list of missing images
  if (!(missImgs.indexOf(imgNum) === -1) || imgNum > numImgs){
    // move on to the next image number if so
    return false;
  }
  return true;
}

// function to generate image path
function imgPath(imgNum){
  // check if image number needs zero padding
  if (imgNum < 10) {
    imgNum = '0' + imgNum;
  } else {
    imgNum = String(imgNum);
  }
  // add properly padded number to path and return
  return 'images/pdxcg_' + imgNum + '.jpg';
}

// function to generate new li containing image
function genImg(imgNum){
  // generate new li
  var newLi = document.createElement('li'),
      newImg = document.createElement('img');// generate new img
  // insert proper src attribute
  newImg.src = imgPath(imgNum);
  // insert image into li
  newLi.appendChild(newImg);
  // return completed element
  return newLi;
}

// function to populate gallery
function popGallery(numImgs) {
  // retreive the gallery element
  var gallery = document.getElementById('gallery');
  // loop once for each image
  for (var i = 1; i <= numImgs; i++){
    // check if image number is valid
    if (!imgExists(i, numImgs)) {
      continue;
    }
    // call generate for the appropriate image number
    // append generated element to gallery
    gallery.appendChild(genImg(i));
  }
}

// function to parse username from url
function getUserName() {
  // check the url and store it in a variable so we can search it
  var pageURL = window.location.href,
      uNameRegEx = /[?&]+([^?&]+)/g, // regex to match strings after ? in url
      passedData = pageURL.match(uNameRegEx); // cache all the matching strings
  // search the match data for the passed username and return it
  for (var i = 0; i < passedData.length; i++) {
    var currStr = passedData[i];
    // match function returns array, loop through that array to find username
    if (currStr.substr(0, 9) === '?username') {
      // break the loop when we find the username
      return currStr.substr(10)
    }
  }
}

// function to insert the username into the page
function popUName(uName) {
  // select the tagline text property and cache it so we can modify it
  var tagLine = document.getElementsByClassName('tagline')[0];
  // modify the cached text property to include the username
  tagLine.innerText = tagLine.innerText + ', ' + uName;
}

// function to select clicked image and display in lightbox
function imgClick(event) {
  // cache the lightbox div
  var lightBox = document.getElementById('image_show'),
  // determine which image was clicked
      clickTarget = event.target,
      imgPath;
  // add event listener to close lightbox div
  document.addEventListener('click', closeLightbox, 'false');
  // check if the lightbox is already displayed
  if (!lightBox.className.match('display_none')) {
    // if so, close the lightbox
    closeLightbox();
    return;
  }
  // get the proper URL for that image

  if (clickTarget.tagName.toLowerCase() === 'img') {
    imgPath = clickTarget.src;
  } else {
    imgPath = clickTarget.childNodes[0].src;
  }
  // change the lightbox img target url
  lightBox.querySelector('img').src = imgPath;
  // remove class that hides lightbox div
  lightBox.classList.remove('display_none');
  // add class that displays lightbox div
  lightBox.classList.add('display_img');
}

// function to close lightbox on a click elsewhere
function closeLightbox(event) {
  // cache the lightbox div
  var lightBox = document.getElementById('image_show'),
      clickTarget = event.target;
  // check to see if the click was on the lightbox image
  if (clickTarget.parentNode.id === 'image_show' &&
      clickTarget.tagName === 'IMG') {
        return; // exit function
  }
  // add class that hides lightbox div
  lightBox.classList.add('display_none');
  // remove class that displays lightbox div
  lightBox.classList.remove('display_img');
  // remove event listener to close lightbox div
  document.removeEventListener('click', closeLightbox, 'false');
}

window.onload = function(){
  var userName = getUserName(), // parse url for username to insert into page
      totalImgs = 60, // total number of images in img folder
      galleryImgs;
  popUName(userName); // fill in userName
  popGallery(totalImgs); // fill in images from img folder
  galleryImgs = document.querySelectorAll('#gallery li'); // get all images
  for (var i = 0; i < galleryImgs.length; i++) {
    // attach handler to each image to bring it to focus
    galleryImgs[i].addEventListener('click', imgClick, 'false');
  }
};
