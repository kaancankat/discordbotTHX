import discord

from discord.ext import commands

bot = commands.Bot(command_prefix= "!" , intents= discord.Intents.all())

@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
    
bot.run("MTE1MDA3NzkwNTc2Njk5Mzk3MA.GoS0fb.Gx1N0NkioYP7cmPBCuIBWrVJe2TC0fh14xObHs")

r = open(playmusic.py,"r").read()

