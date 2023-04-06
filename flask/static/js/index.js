$("#my-button").click(function() {
    const channel_cible = $("#channel_cible").val();
    const message = $("#message").val();

    $.ajax({
        url: '/download_custom_message',
        type: 'POST',
        data: {
            param1: channel_cible,
            param2: message
        },
        success: function(response) {
            $("#result-container").html(response.result);
        },
        error: function() {
            alert("Erreur lors de l'appel de la fonction Python.");
        }
    });
});