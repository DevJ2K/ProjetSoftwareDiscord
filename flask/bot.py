import nextcord
import os
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.get_channel(1091449953047543852).send("Yo je suis All-In-One !")
    print(f"{bot.user} est connecté.")

# Ajoutez vos commandes ici.
async def send_message(channel: int, message: str):
    await bot.get_channel(channel).send(message)
    # print(f"{bot.user} est connecté.")

async def run_bot(token):
    await bot.start(token)