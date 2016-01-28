// this page requires a cycling jumbotron that moves between images in the
// image is set using background image property in css, so this script
// will modify the css for the .jumbotron element

// function to change the css background image target of an element
function backImgChng(target, num) {
  // num is image number, image is targeted dom element, numstring is conversion
  var numstring = num.toString();
  // oh noes, we're missing an image! Lets fix that problem
  if (num === 42) {
    num++;
  }
  // pad image identifying number so it will work with concatenation below
  if (num < 10) {
    numstring = '0' + numstring;
  }
  // change the image with css
  target.style.backgroundImage = 'url("images/pdxcg_' + numstring + '.jpg")';
}

// loop function to select image and call change function every 10 seconds
function imageSelector() {
  var imgNum = 1, // set initial image value
      totImg = 60, // store the highest image number
      jumbotron = document.getElementById('jumbotron');
  // select a new number and call the image change function every 10 seconds
  window.setInterval(function() {
    imgNum++;
    if (imgNum > totImg) {
      imgNum = 1;
    }
    backImgChng(jumbotron, imgNum);
  }, 10000);
}

// window load function to call above functions
window.onload = function() {
  imageSelector();
};
