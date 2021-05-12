let movie;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (movie of data.results) {
    $('#list_movies').append($('<li></li>').text(movie.title));
  }
});
