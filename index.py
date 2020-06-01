import time
import discord
from discord.ext import commands
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix='!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def setup(ctx):
    embed = discord.Embed(title='🛠\t|\tFirst steps\t|\t🛠', color=discord.Color.blue())
    embed.add_field(name='How can i start?', value='Use "start followed by a space with the name of the server you want to track, for example: !start server.net',inline=False)
    embed.add_field(name='How long does it take to report the status of the server?', value='Every 45 minutes it sends a message about the status of the server')
    embed.set_footer(text='Something is wrong? feel free to contact me: CroagSenpai#2058')
    await ctx.send(embed=embed)


@bot.command()
async def start(ctx, servidor):
    server = MinecraftServer.lookup(servidor)
    while True:
        try:
            status = server.status()
            await ctx.send('El servidor está abierto con {} jugadores({0}) y un ping de {} ms'.format(status.players.online, round(status.latency)))
        except:
            await ctx.send('El servidor está cerrado')
        finally:
            time.sleep(2700)


@bot.event
async def on_ready():
    game = discord.Game('!setup to start')
    await bot.change_presence(activity=game)



bot.run(yourtoken)
