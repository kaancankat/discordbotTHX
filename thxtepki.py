import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    target_channel_id = 891738544522035230

    if message.channel.id == target_channel_id:
        await message.add_reaction('👍') 
        await message.add_reaction('👎')
        
bot.run("MTA4MTk5NDQ5NjI1NTk4MzcyNw.GSzi6h.EkiQ7tqsXuGlg0n_xyNl6VJfj4OsBgr3DKRfF4")