import os
import random
import nextcord
from nextcord.ext import commands
# from nextcord.utils import get
from nextcord import ButtonStyle
from nextcord.ui import Button, View, Modal, Select
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.message_content = True

client = nextcord.Client(intents=intents)

liste_mot_blacklist = [
    "test"
]

reponse_gros_mots = [
    "Oh ton langage {} ! C'est pas la cité ici donc parle bien.",
    "Tu parles mal {} il va falloir te calmer !",
    "Tu es bien grossier dis donc {} !",
    "Orhhhhhhh {} je vais devoir te dire combien de fois de te calmer !?"
]


channel_cible = 1091449953047543852

@client.event
async def on_ready():
    print("En ligne")

@client.event
async def on_message(message: nextcord.Message):
    for mot_blacklist in liste_mot_blacklist:
        if mot_blacklist in message.content.lower():
            print("insulte présent")
            await message.reply(random.choice(reponse_gros_mots).format(message.author.mention))
            await message.delete()
            return

        elif "@everyone" in message.content.lower() and channel_cible not in [i.id for i in message.author.roles]:  # type: ignore
            print("@everyone présent")
            await message.reply(f"{message.author.mention} ne mentionne pas tout le monde s'il te plait ça dérange tout le monde...")
            await message.delete()
            return

    

    if message.content.split(" ")[-1].lower() == "quoi":
        await message.reply("FEUR !")
        return

    if channel_cible in [i.id for i in message.author.roles]: #MESSAGE OWNER
        if message.content.lower().startswith("ftg"):
            pseudo = message.content.split(" ")[-1]
            pseudo = client.get_user(int(pseudo[2:-1]))

            await message.channel.send(f"C'est réel {pseudo.mention} ftg arrête d'aboyer.")
            await pseudo.send(f"T'as intérêt à te calmer dans le serveur {pseudo.mention} parce que là tu clc en vrai. Donc tg stp.")
            for _ in range(7):
                await pseudo.send(f"C'est un mini spam de prévention {pseudo.mention}, je peux aller jusqu'à ... BEAUCOUP !!")

        
        elif message.content.lower().startswith("fais taire"):
            pass
            
        elif message.content.lower().startswith("Arrête d'aboyer"):
            pass

# bot.run(os.getenv("TOKEN"))
client.run("MTA5MTQ0ODYwNTg3OTA0MjEyNg.GIYSE6.DGcMh33Ksv_Z4VGVpkJGPw2lU9ejcqD1S-QcS0")