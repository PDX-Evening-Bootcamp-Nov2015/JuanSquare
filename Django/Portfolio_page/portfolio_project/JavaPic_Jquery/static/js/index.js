// this page requires a cycling jumbotron that moves between images in the
// image is set using background image property in css, so this script
// will modify the css for the .jumbotron element

import imgPath from 'gallery';
import getNumImgs from 'gallery';

/* function to change the css background image target of an element */
function backImgChng($target, num) {
  var url = imgPath(num);
  // change the image with css
  $target.css('background-image', 'url("' + url + '")');
}

/* loop function to select image and call change function every 10 seconds */
function imageSelector() {
  var imgNum = 1, // set initial image value
      totImg = getNumImgs(), // store the highest image number
      $jumbotron = $('.jumbotron');
  // select a new number and call the image change function every 10 seconds
  window.setInterval(function() {
    imgNum++;
    if (imgNum > totImg) {
      imgNum = 1;
    }
    backImgChng($jumbotron, imgNum);
  }, 10000);
}

/* window load function to call above functions */
$(function(){
  imageSelector();
});
