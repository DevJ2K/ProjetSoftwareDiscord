function afficher() {
    var a = document.getElementById("accueil").style.display = "block"
}
function cacher() {
    var a = document.getElementById("accueil").style.display = "none"
}
function afficher2() {
    var b = document.getElementById("bots").style.display = "block"
}
function cacher2() {
    var b = document.getElementById("bots").style.display = "none"
}
function afficher3() {
    var d = document.getElementById("db").style.display = "block"
}
function cacher3() {
    var d = document.getElementById("db").style.display = "none"
}

async function sendMessage() {
    const message = document.getElementById('message').value;
    const channel = document.getElementById('channel').value;
    const response = await fetch('/send_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'message': message, 'channel': channel }),
    });

    if (response.ok) {
        alert('Message envoyé');
    } else {
        alert('Erreur lors de l\'envoi du message');
    }
}