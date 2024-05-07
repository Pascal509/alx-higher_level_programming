$(document).ready(function() {
    // Function to fetch and display the greeting
    function fetchAndDisplayGreeting() {
        var langCode = $("#language_code").val();  // Get the language code from the input
        var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";  // API endpoint

        // Perform the AJAX GET request
        $.get(apiUrl, { lang: langCode }, function(response) {
            $("#hello").text(response.hello);  // Display the greeting in DIV#hello
        }).fail(function() {
            $("#hello").text("Failed to retrieve greeting.");  // Error handling
        });
    }

    // Event handler for clicking the translate button
    $("#btn_translate").click(fetchAndDisplayGreeting);

    // Event handler for pressing ENTER in the language code input
    $("#language_code").keypress(function(event) {
        if (event.which === 13) {  // Check if the key pressed is the ENTER key
            fetchAndDisplayGreeting();
        }
    });
});
