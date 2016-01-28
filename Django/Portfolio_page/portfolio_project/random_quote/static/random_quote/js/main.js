/*
Requirements:
This document will make an AJAX request to a quote database API and display
that quote on the page. This will require:
  - A function to create each new AJAX request
  - A function to parse each new ajax request
  - A function to populate the page with each new ajax request

  API Address: http://quotesondesign.com/api/3.0/api-3.0.json
  or just ../api-3.0.json if using Garret's server trick
*/

// function to create each new AJAX request
function newRequest() {
  // initialize a new ajax request object
  var newReq = new XMLHttpRequest();
  // attach function for when request is complete and successful
  newReq.onreadystatechange = function() {
    if (newReq.readyState === 4 && newReq.status === 200) {
      // pass data to the parsing function
      parseRequest(newReq.responseText);
    }
  }
  // set paratmeters for request
  newReq.open('GET', 'http://54.68.253.162/StudentWork/api-3.0.json', true);
  // send the request
  newReq.send();
}


// function to parse each new ajax request
function parseRequest(quoteData) {
  // take quote data and get a quote out
  var response = JSON.parse(quoteData);
  // pull out the actual quote
  quote = response.quote;
  // pass quote to the html populating function
  populateQuote(quote);
}


// function to populate the page with each new ajax request
function populateQuote(quote) {
  // select the paragraph inside the quote box
  var quoteSpace = document.getElementById('quote_space');
  // modify the paragraph to contain the required quote
  quoteSpace.innerText = quote;
}



// page loaded initializations
function initialize() {
  var reqQuoteButton = document.getElementById('get_inspired');
  reqQuoteButton.addEventListener('click', newRequest, false);
}
window.onload = initialize;
