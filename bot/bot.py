import discord
from discord.ext import commands, tasks
from dotenv import dotenv_values

load_dotenv = dotenv_values("./bot/.env")
TOKEN = load_dotenv["DISCORD_TOKEN"]
PREFIX = load_dotenv["DISCORD_PREFIX"]

bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="-help"))


  
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("❌ Invalid command. Please use **`-help`** for a list of available commands.")

bot.run(TOKEN)