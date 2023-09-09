import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= "!" , intents= discord.Intents.all())

@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
  
@bot.command()  
async def midpoint(ctx):
    await ctx.send("geçen gün midpointe gittim kaç kişisiniz dediler 2 kişiyim dedim ben ve Allah")

@bot.command()  
async def yiğit(ctx):
    await ctx.send("poşet rank yemin ediyorum bak")
    
@bot.command()  
async def azmi(ctx):
    await ctx.send("enayi")




#deleted mesage#

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı!')

@bot.command()
async def clear(ctx, amount: int):
    if 0 < amount <= 1000:
        await ctx.message.delete()  
        await ctx.channel.purge(limit=amount)  
    else:
        await ctx.send("Lütfen 1 ile 1000 arasında bir sayı belirtin.")






bot.run("MTE1MDA3NzkwNTc2Njk5Mzk3MA.GhodzL.7Q1t7oHCa41AUqulsIQTaR6ZVYW6lDFVOMLftk")