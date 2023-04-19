import nextcord
import os
from nextcord.ext import commands
import threading
import platform

systemeExploitation = platform.system()


intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.bans = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot_ready = threading.Event()

@bot.event
async def on_ready():
    await bot.get_channel(1091449953047543852).send("Yo je suis All-In-One !")
    print(f"{bot.user} est connecté.")
    bot_ready.set()
   


# @bot.event
# async def on_message(message):
#     print(message.content)
#     print(f"{bot.user} est connecté et prêt à recevoir des messages.")


# Ajoutez vos commandes ici.
async def send_message(message, channel=None):
    channel = 1091449953047543852
    await bot.get_channel(int(channel)).send(str(message))

    # print(f"{bot.user} est connecté.")

async def send_embed(channel, couleur, titre, desc, fieldName, fieldDesc):
    embed = nextcord.Embed(title=titre, description=desc, color=0xFF00FF)
    embed.add_field(name=fieldName, value=fieldDesc)
    await bot.get_channel(1091449953047543852).send(embed=embed)




def getStats():
    nombre_de_serveurs = len(bot.guilds)
    membres_des_serveurs = {}
    for guild in bot.guilds:
        membres_des_serveurs[guild.name] = [[f"{member.display_name}#{member.discriminator}" for member in guild.members], guild.member_count]
    return {
        "nombre_de_serveurs": nombre_de_serveurs,
        "membres_des_serveurs": membres_des_serveurs
    }


def run_windows_bot(token):
    bot.run(token)
    return getStats()

async def run_mac_bot(token):
    await bot.start(token)



if __name__ == "__main__":
    if systemeExploitation == "Windows":
        run_windows_bot("MTA5MTQ0ODYwNTg3OTA0MjEyNg.Gj_vsL.Q0utWzTCSf8yZXz05012P2TXQcTyjT5ure1OKY")

__all__ = ["run_windows_bot", "getStats", "bot_ready"]
