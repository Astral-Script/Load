import discord
from discord.ext import commands
import os

# --- CONFIG ---
TOKEN = os.getenv("BOT_TOKEN")
# Your GitHub script
MY_SCRIPT = 'loadstring(game:HttpGet("[https://raw.githubusercontent.com/CStudios-Dev/csLoader.lua/main/CSLoader.lua](https://raw.githubusercontent.com/CStudios-Dev/csLoader.lua/main/CSLoader.lua)"))()'
# Your new purple logo link
IMAGE_URL = "[https://cdn.discordapp.com/attachments/1424784310418014360/1456699055244710094/Screenshot_2026-01-03-01-19-35-95_680d03679600f7af0b4c700c6b270fe7.jpg](https://cdn.discordapp.com/attachments/1424784310418014360/1456699055244710094/Screenshot_2026-01-03-01-19-35-95_680d03679600f7af0b4c700c6b270fe7.jpg)" 
# --------------

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix="!", intents=intents)

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Mobile Copy", style=discord.ButtonStyle.secondary, emoji="🟣")
    async def copy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # We removed the ``` so it copies the raw text only
        # Sending as a 'hidden' message so only you see it
        await interaction.response.send_message(content=MY_SCRIPT, ephemeral=True)

@bot.command()
async def loader(ctx):
    # Purple Embed
    embed = discord.Embed(
        title="Zenith Studios Loader", 
        description=f"```lua\n{MY_SCRIPT}```",
        color=0x8A2BE2 
    )
    embed.set_thumbnail(url=IMAGE_URL)
    embed.add_field(
        name="Mobile Instructions", 
        value="1. Tap the **Mobile Copy** button.\n2. Long-press the hidden message that appears.\n3. Tap **Copy Text**.", 
        inline=False
    )
    await ctx.send(embed=embed, view=Menu())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!loader"))
    print(f"Logged in as {bot.user}")

if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: BOT_TOKEN Environment Variable is missing!")
