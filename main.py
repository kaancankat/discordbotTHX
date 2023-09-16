import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Store voice clients and voice channels
voice_clients = {}
voice_channels = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    target_channel_id = 891738544522035230

    if message.channel.id == target_channel_id:
        await message.add_reaction('👍')
        await message.add_reaction('👎')

    await bot.process_commands(message)  # Bu satır, komutların işlenmesi için gerekli

@bot.command()
async def play(ctx, *, query):
    try:
        voice_state = ctx.author.voice
        if voice_state is not None:
            voice_channel = voice_state.channel
            if ctx.guild.id in voice_clients:
                await voice_clients[ctx.guild.id].move_to(voice_channel)
            else:
                voice_client = await voice_channel.connect()
                voice_clients[ctx.guild.id] = voice_client
                voice_channels[ctx.guild.id] = voice_channel
        else:
            await ctx.send("Bu komutu kullanmak için bir ses kanalında olmalısınız.")
            return

    except Exception as err:
        print(err)

    try:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(query, download=False))
        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    except Exception as err:
        print(err)

@bot.command()
async def pause(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as err:
        print(err)

@bot.command()
async def resume(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as err:
        print(err)

@bot.command()
async def stop(ctx):
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
        # Remove the channel from the dictionary when the bot leaves
        del voice_channels[ctx.guild.id]
    except Exception as err:
        print(err)

@bot.command()
async def say(ctx, *, message_to_repeat):
    await ctx.message.delete()
    await ctx.send(message_to_repeat)

@bot.command()
async def clear(ctx, count: int):
    try:
        deleted = await ctx.channel.purge(limit=count + 1)
        await ctx.send(f"Deleted {len(deleted) - 1} messages.")
    except Exception as err:
        print(err)

@bot.command()
async def midpoint(ctx):
    response = "Geçen gün midpointe gittim, kaç kişisiniz dediler, 2 kişiyim dedim, ben ve Allah döndürsün."
    await ctx.send(response)

@bot.command()
async def yiğit(ctx):
    response = "poşet rank"
    await ctx.send(response)

@bot.command()
async def talha(ctx):
    response = "卍卍卍卍卍卍卍卍卍卍"
    await ctx.send(response)

@bot.command()
async def emre(ctx):
    response = "enayi gay lolcü hayatsız"
    await ctx.send(response)

@bot.command()
async def mizan(ctx):
    response = "o/"
    await ctx.send(response)

@bot.command()
async def akdere(ctx):
    response = "5 ay enayilikten sonra bizim sıfat"
    await ctx.send(response)

#@bot.event
#async def on_voice_state_update(member, before, after):
#    if member.guild.id in voice_clients:
#        if voice_channels[member.guild.id] != after.channel:
#            await voice_clients[member.guild.id].move_to(after.channel)

bot.run("MTE1MDA3NzkwNTc2Njk5Mzk3MA.GX-Sjz.AgDOAJEbT5nvd9K52I-hbkDGMBwB3k8-yOqFeM")