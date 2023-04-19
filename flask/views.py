from quart import Quart, render_template, request, jsonify
import threading
import bot
import platform
import asyncio
from bot import run_windows_bot, getStats, bot_ready

systemeExploitation = platform.system()

def read_from_config(file_path, params):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(f"{params}="):
                return line.strip().split('=')[1]

if systemeExploitation == "Windows":    
    token = read_from_config("config.txt", "TOKEN")

if systemeExploitation == "Darwin": #MacOS
    token = "" 


app = Quart(__name__)

@app.route('/')
async def index():
    # return await render_template('index.html', nombre_de_serveurs=statistiques['nombre_de_serveurs'], liste_serveur= ",\n".join([i for i in statistiques['membres_des_serveurs']]))   
    return await render_template('index.html')


@app.route('/start_bot', methods=['POST'])
async def start_bot():
    if systemeExploitation == "Windows":
        t = threading.Thread(target=bot.run_windows_bot, args=(token,))
        t.start()
    elif systemeExploitation == "Darwin":
        asyncio.run_coroutine_threadsafe(bot.run_mac_bot(token), asyncio.get_event_loop())
    
    return 'Bot démarré'
    

@app.route('/send_message', methods=['POST'])
async def send_message():
    data = await request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({'error': 'Message vide'}), 400

    if systemeExploitation == "Windows":
        loop = bot.bot.loop
        loop.create_task(bot.send_message(message=message))
    elif systemeExploitation == "Darwin":
        asyncio.run_coroutine_threadsafe(bot.send_message(message=message), asyncio.get_event_loop())

    return jsonify({'success': 'Message envoyé'}), 200


@app.route('/send_embed', methods=['POST'])
async def send_embed():
    data = await request.get_json()
    channel = data.get('channel', '')
    titre = data.get('titre', '')
    description = data.get('description', '')
    fieldName = data.get('fieldName', '')
    fieldValue = data.get('fieldValue', '')

    # if not message:
    #     return jsonify({'error': 'Message vide'}), 400

    if systemeExploitation == "Windows":
        loop = bot.bot.loop
        loop.create_task(bot.send_embed(channel=channel, couleur="", titre=titre, desc=description, fieldName=fieldName, fieldDesc=fieldValue))
    elif systemeExploitation == "Darwin":
        asyncio.run_coroutine_threadsafe(bot.send_embed(channel=channel, couleur="", titre=titre, desc=description, fieldName=fieldName, fieldDesc=fieldValue), asyncio.get_event_loop())

    return jsonify({'success': 'Embed envoyé'}), 200 


# if __name__ == '__main__':
if systemeExploitation == "Windows":
    t = threading.Thread(target=bot.run_windows_bot, args=(token,))
    t.start()

    bot_ready.wait()

    statistiques = bot.getStats()
    print(statistiques)



app.run(debug=True)
