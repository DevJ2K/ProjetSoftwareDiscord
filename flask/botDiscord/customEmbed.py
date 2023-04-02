import os
import nextcord
from nextcord.ext import commands
# from nextcord.utils import get
from nextcord import ButtonStyle
from nextcord.ui import Button, View, Modal, Select
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")
TOKEN = "MTA5MTQ0ODYwNTg3OTA0MjEyNg.GIYSE6.DGcMh33Ksv_Z4VGVpkJGPw2lU9ejcqD1S-QcS0"

# channel_cible = int(input("Quelle est le channel cible : "))

# titre_embed = input("Titre : ")
# desc_embed = input("Description : ")

# sous_titre1 = input("Sous-titre 1 : ")
# desc_titre1 = input("Description sous-titre 1 : ")


intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
    print("Bot en ligne !")

async def sendEmbed(channel_cible, titre_embed, desc_embed, sous_titre, desc_titre):
    embed = nextcord.Embed(title=titre_embed, description=desc_embed, color=0xFF00FF)
    embed.add_field(name=sous_titre, value=desc_titre)
    await bot.get_channel(channel_cible).send(embed=embed)      #type: ignore

# bot.run(os.getenv("TOKEN"))
bot.run(TOKEN)