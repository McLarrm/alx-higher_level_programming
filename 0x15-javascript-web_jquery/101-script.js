$(document).ready(function () {
  // Add item to the list
  $('#add_item').click(function () {
    // Create a new <li> element with text "Item"
    var newItem = $('<li>Item</li>');

    // Append the new <li> element to the UL with class my_list
    $('ul.my_list').append(newItem);
  });

  // Remove the last item from the list
  $('#remove_item').click(function () {
    // Select the last <li> element within the UL
    var lastItem = $('ul.my_list li:last-child');

    // Remove the last <li> element
    lastItem.remove();
  });

  // Clear all items from the list
  $('#clear_list').click(function () {
    // Remove all <li> elements within the UL
    $('ul.my_list').empty();
  });
});
