import os
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

# utilisateurID = int(input("ID de l'utilisateur : "))
utilisateurID = 1022192517753614336
# message = input("Le message : ")
message = "Salut"

@bot.event
async def on_ready():
    print(await bot.get_user(utilisateurID).display_name)



# bot.run(os.getenv("TOKEN"))
bot.run("MTA5MTQ0ODYwNTg3OTA0MjEyNg.GIYSE6.DGcMh33Ksv_Z4VGVpkJGPw2lU9ejcqD1S-QcS0")