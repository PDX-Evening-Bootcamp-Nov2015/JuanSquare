/*
Requirements:
This document will make an AJAX request to a quote database API and display
that quote on the page. This will require:
  - A function to create each new AJAX request
  - A function to parse each new ajax request
  - A function to populate the page with each new ajax request

  API Address: http://quotesondesign.com/api/3.0/api-3.0.json
  or just ../api-3.0.json if using Garretr's server trick
*/

/* function to create each new AJAX request */
function newRequest() {
  // initialize a new ajax request object
  var settings = {
    method: 'GET',
    url: 'http://quotesondesign.com/api/3.0/api-3.0.json',
    dataType: 'jsonp',
    success: populateQuote
  };
  $.ajax(settings);
}


/* function to populate the page with each new ajax request */
function populateQuote(quote) {
  // select the paragraph inside the quote box
  var $quoteSpace = $('#quote_space');
  // modify the paragraph to contain the required quote
  $quoteSpace.text(quote.quote);
}



/* page loaded initializations */
function initialize() {
  var $reqQuoteButton = $('#get_inspired');
  $reqQuoteButton.click(newRequest);
}
$(initialize);
