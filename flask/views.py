from flask import Flask, render_template, request, jsonify
import glob
import random

from botDiscord import customEmbed
# -*- coding: utf-8 -*-

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

# app.py
@app.route('/execute_function', methods=['POST'])
def execute_function():
    param1 = request.form.get('channel_cible')
    param2 = request.form.get('titre_embed')
    param3 = request.form.get('desc_embed')
    param4 = request.form.get('sous_titre')
    param5 = request.form.get('desc_titre')

    # Exécutez votre fonction avec les paramètres
    
    result = my_python_function(param1, param2, param3, param4, param5)
    return jsonify(result=result)

async def my_python_function(param1, param2, param3, param4, param5):
    # Votre fonction Python avec des paramètres
    await customEmbed.sendEmbed(param1, param2, param3, param4, param5)
    return f"L'embed a bien été envoyé !"


if __name__ == '__main__':
    app.run(debug=True)
