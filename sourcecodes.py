import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="sc/")

@bot.command()
async def search(ctx, lang):
  if lang in ["py","js","rb","java","php","json"]:
    print("a")
