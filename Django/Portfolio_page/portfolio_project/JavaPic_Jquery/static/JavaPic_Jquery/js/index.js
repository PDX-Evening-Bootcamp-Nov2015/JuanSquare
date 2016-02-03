// this page requires a cycling jumbotron that moves between images in the
// image is set using background image property in css, so this script
// will modify the css for the .jumbotron element

/* function to generate image path
    NOTE: this function assumes files follow a naming convention with
    two-digit, zero-padded integers */
function imgPath(imgNum) {
  imgNum = String(imgNum);
  // check if image number needs zero padding
  if (imgNum.length < 2) {
    imgNum = '0' + imgNum;
  }
  // add properly padded number to path and return
  return '/static/JavaPic_Jquery/images/pdxcg_' + imgNum + '.jpg';
}

/* function to change the css background image target of an element */
function backImgChng($target, num) {
  var url = imgPath(num);
  // change the image with css
  $target.css('background-image', 'url("' + url + '")');
}

/* loop function to select image and call change function every 10 seconds */
function imageSelector() {
  var imgNum = 1, // set initial image value
    totImg = 60, // store the highest image number
    $jumbotron = $('.jumbotron');
  // select a new number and call the image change function every 10 seconds
  console.log(totImg);
  window.setInterval(function() {
    imgNum++;
    if (imgNum > totImg) {
      imgNum = 1;
    }
    backImgChng($jumbotron, imgNum);
  }, 10000);
}

/* window load function to call above functions */
$(function() {
  imageSelector();
});
