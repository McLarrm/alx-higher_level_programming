$(document).ready(function() {
  // Make an AJAX GET request to the SWAPI URL for movies
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results; // Get the list of movies from the response data

    // Get the HTML <ul> element with the id "list_movies"
    var $listMovies = $('#list_movies');

    // Loop through the movies and add each title to the <ul>
    $.each(movies, function(index, movie) {
      // Create an <li> element for the movie title
      var $movieItem = $('<li>').text(movie.title);

      // Append the <li> element to the <ul>
      $listMovies.append($movieItem);
    });
  });
});
