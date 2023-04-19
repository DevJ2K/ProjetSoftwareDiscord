async function startBot() {
    await fetch('/start_bot', { method: 'POST' });
    alert('Bot démarré');
}

async function stopBot() {
    await fetch('/stop_bot', { method: 'POST' });
    alert('Bot arrêté');
}

async function sendMessage() {
    const message = document.getElementById('message').value;
    const response = await fetch('/send_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'message': message }),
    });

    if (response.ok) {
        alert('Message envoyé');
    } else {
        alert('Erreur lors de l\'envoi du message');
    }
}

async function sendEmbed() {
    const channel = document.getElementById('channel').value;
    const titre = document.getElementById('titre').value;
    const description = document.getElementById('description').value;
    const fieldName = document.getElementById('fieldName').value;
    const fieldValue = document.getElementById('fieldValue').value;

    const response = await fetch('/send_embed', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            'channel': channel, 
            'titre': titre,
            'description': description,
            'fieldName': fieldName,
            'fieldValue': fieldValue
    }),
    });

    if (response.ok) {
        alert('Message envoyé');
    } else {
        alert('Erreur lors de l\'envoi du message');
    }
}