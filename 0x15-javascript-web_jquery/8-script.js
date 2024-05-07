$(document).ready(function() {
    // Perform an AJAX request to fetch movie titles
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        // Iterate over each film in the received data
        $.each(data.results, function(index, film) {
            // Append a new <li> for each film's title to the UL with id 'list_movies'
            $("#list_movies").append($('<li>').text(film.title));
        });
    }).fail(function() {
        console.log("Error fetching data.");
    });
});
