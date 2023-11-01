$(document).ready(function() {
  // Make an AJAX GET request to the specified URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Get the translation of "hello" from the response
    var translation = data.hello;

    // Get the HTML <div> element with the id "hello"
    var $helloDiv = $('#hello');

    // Set the translation as the text content of the <div>
    $helloDiv.text(translation);
  });
});
