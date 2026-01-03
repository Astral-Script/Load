import discord
from discord.ext import commands
import os

# --- CONFIG ---
TOKEN = os.getenv("BOT_TOKEN")
MY_SCRIPT = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/CStudios-Dev/csLoader.lua/main/CSLoader.lua"))()'
# Use your updated purple logo link
IMAGE_URL = "https://cdn.discordapp.com/attachments/1424784310418014360/1456699055244710094/Screenshot_2026-01-03-01-19-35-95_680d03679600f7af0b4c700c6b270fe7.jpg" 
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
        # Sends raw script for 1-tap copy on mobile
        await interaction.response.send_message(content=MY_SCRIPT, ephemeral=True)

@bot.command()
async def loader(ctx):
    embed = discord.Embed(
        title="Carbon Studios Loader", 
        description=f"```lua\n{MY_SCRIPT}```",
        color=0x8A2BE2  # Exact Purple
    )
    embed.set_thumbnail(url=IMAGE_URL)
    embed.add_field(
        name="Mobile Instructions", 
        value="1. Tap **Mobile Copy**.\n2. Long-press the hidden message.\n3. Tap **Copy Text**.", 
        inline=False
    )
    await ctx.send(embed=embed, view=Menu())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!loader"))
    print(f"Logged in as {bot.user}")

if TOKEN:
    bot.run(TOKEN)
