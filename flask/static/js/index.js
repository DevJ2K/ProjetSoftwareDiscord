$("#my-button").click(function() {
    const param1 = $("#param1").val();
    const param2 = $("#param2").val();

    $.ajax({
        url: '/execute_function',
        type: 'POST',
        data: {
            param1: param1,
            param2: param2
        },
        success: function(response) {
            $("#result-container").html(response.result);
        },
        error: function() {
            alert("Erreur lors de l'appel de la fonction Python.");
        }
    });
});