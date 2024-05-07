$(document).ready(function() {
    // Event handler for button click
    $("#btn_translate").click(function() {
        // Get the language code from the input
        var langCode = $("#language_code").val();
        // Construct the URL for the API request
        var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";
        // Fetch the greeting using the language code
        $.get(apiUrl, { lang: langCode }, function(response) {
            // Display the fetched "hello" in the DIV#hello
            $("#hello").text(response.hello);
        }).fail(function() {
            $("#hello").text("Failed to retrieve greeting.");
        });
    });
});
