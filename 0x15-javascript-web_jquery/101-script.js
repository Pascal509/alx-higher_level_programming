$(document).ready(function(){
    $("#add_item").click(function(){
        $("ul.my_list").append("<li>Item</li>");
    });

    // Remove the last item of the list when DIV#remove_item is clicked
    $("#remove_item").click(function() {
        $("ul.my_list li:last").remove();
    });

    // Clear all items from the list when DIV#clear_list is clicked
    $("#clear_list").click(function() {
        $("ul.my_list").empty();
    });
});