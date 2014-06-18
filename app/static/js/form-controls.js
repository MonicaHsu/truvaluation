// jQuery code for querying/filtering data based on form controls

// Updates the slider when input text values are changed.
$("#min_price-textbox, #beds-textbox").on("change", function() {
    var priceChange = $("#min_price-textbox").val(),
        bedsChange = $("#beds-textbox").val(),

    $("#min_list_price").val(priceChange);
    $("#beds").val(bedsChange);
});

// Submits form when slider is moved.
$("#min_price-textbox, #beds-textbox").on("change", function() {
    $("#form").submit();
});

// Reset form to default values.
$("#reset").on("click", function() {
    // Set slider values to default.
    $("#min_list_price").val(1000000);
    $("#beds").val(3);

    // Default order and sort by
    $("#order_by").val("difference");
    $("#sort").val("ASC");

    // Submit form
    $("#form").submit();
});
