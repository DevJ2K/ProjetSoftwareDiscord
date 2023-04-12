from quart import Quart, render_template, request, jsonify
import threading
import bot
import asyncio
import configparser

def read_token_from_config(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("TOKEN="):
                return line.strip().split('=')[1]

# Récupérer le token à partir de la section et de la clé appropriées
token = read_token_from_config("config.txt")


# from botDiscord import customEmbed
# -*- coding: utf-8 -*-

app = Quart(__name__)

@app.route('/')
async def index():
    t = threading.Thread(target=bot.run_bot, args=(token,))
    t.start()
    return await render_template('index.html')


@app.route('/send_message', methods=['POST'])
async def send_message():
    data = await request.get_json()
    message = data.get('message', '')
    channel = data.get('channel', '')

    if not message:
        return jsonify({'error': 'Message vide'}), 400

    loop = bot.bot.loop
    loop.create_task(bot.send_message(channel=channel, message=message))

    return jsonify({'success': 'Message envoyé'}), 200


if __name__ == '__main__':
    app.run(debug=True)
