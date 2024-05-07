$(document).ready(function() {
    // When the div with id 'add_item' is clicked
    $("#add_item").click(function() {
        // Append a new <li> element to the <ul> with class 'my_list'
        $("ul.my_list").append("<li>Item</li>");
    });
});
