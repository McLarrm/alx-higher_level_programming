$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    var languageCode = $('#language_code').val();

    // Make an AJAX GET request to the API
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: {
        lang: languageCode,
      },
      success: function (response) {
        // Display the translation in the HTML tag DIV#hello
        $('#hello').text(response.hello);
      },
    });
  });
});
