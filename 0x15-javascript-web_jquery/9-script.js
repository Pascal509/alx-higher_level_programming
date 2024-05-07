$(document).ready(function() {
    // Fetch data from the URL with a query parameter for French language
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        // Display the 'hello' value in the DIV#hello
        $("#hello").text(data.hello);
    }).fail(function() {
        console.log("Error fetching the greeting.");
    });
});
