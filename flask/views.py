from flask import Flask, render_template, request, jsonify, send_file, make_response
import glob
import random
import shutil
import io


# from botDiscord import customEmbed
# -*- coding: utf-8 -*-

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/")
def accueil():
    return render_template('accueil.html')

# # app.py
@app.route('/download_custom_message', methods=['POST'])
def download_custom_message():
    channel_cible = request.form.get('param1')
    message = request.form.get('param2')
    
    with open("custom_messages_1.py", "w") as f:
        f.write(str(channel_cible))
    
#     # Exécutez votre fonction avec les paramètres
    
#     result = my_python_function(param1, param2, param3, param4, param5)
    # send_file(output)
    return send_file("custom_messages_1.py", as_attachment=True, download_name="CustomMessage.py", mimetype="text/x-python")
    # return jsonify(result="Telechargement effectué")  

# async def my_python_function(param1, param2, param3, param4, param5):
#     # Votre fonction Python avec des paramètres
#     await customEmbed.sendEmbed(param1, param2, param3, param4, param5)
#     return f"L'embed a bien été envoyé !"


if __name__ == '__main__':
    app.run(debug=True)
