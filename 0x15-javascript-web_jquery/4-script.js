$(document).ready(function() {
    // When the div with id 'toggle_header' is clicked
    $("#toggle_header").click(function() {
        // Toggle between 'red' and 'green' classes for the <header> element
        if ($("header").hasClass("red")) {
            $("header").removeClass("red").addClass("green");
        } else {
            $("header").removeClass("green").addClass("red");
        }
    });
});
