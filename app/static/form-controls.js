// jQuery code for querying/filtering data based on form controls

// Updates the slider when input text values are changed.
$("#price-textbox, #beds-textbox").on("change", function() {
    var priceChange = $("#price-textbox").val(),
        bedsChange = $("#beds-textbox").val(),

    $("#price").val(priceChange);
    $("#beds").val(bedsChange);
});

// Submits form when slider is moved.
$("#price-textbox, #beds-textbox").on("change", function() {
    $("#form").submit();
});

// Reset form to default values.
$("#reset").on("click", function() {
    // Set slider values to default.
    $("#price").val(1000000);
    $("#beds").val(3);

    // Default order and sort by
    $("#order_by").val("difference");
    $("#sort").val("ASC");

    // Submit form
    $("#form").submit();
});
