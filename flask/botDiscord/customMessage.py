import os
import time
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

bot = commands.Bot(command_prefix="!", intents=intents)

message = "Yo je suis All-In-One !"
# channel_cible = int(input("Quelle est le channel cible : "))
channel_cible = 1091449953047543852


@bot.event
async def on_ready():
    print("Envoi en cours...")
    await bot.get_channel(channel_cible).send(message)
    print("Message envoyé !")
    time.sleep(2)
    await bot.close()



# bot.run(os.getenv("TOKEN"))
bot.run("MTA5MTQ0ODYwNTg3OTA0MjEyNg.GIYSE6.DGcMh33Ksv_Z4VGVpkJGPw2lU9ejcqD1S-QcS0")