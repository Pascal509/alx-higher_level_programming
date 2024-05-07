$(document).ready(function() {
    // Perform AJAX request to the Star Wars API
    $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
        // Display the fetched character name in the DIV#character
        $("#character").text(data.name);
    }).fail(function() {
        console.log("An error has occurred.");
    });
});
