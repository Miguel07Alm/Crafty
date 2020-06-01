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
    embed.add_field(name='How can i start?', value='Use "!check followed by a space with the name of the server you want to track, for example: !check server.net',inline=False)
    embed.set_footer(text='Something is wrong? feel free to contact me: CroagSenpai#2058')
    await ctx.send(embed=embed)


@bot.command()
async def check(ctx, servidor):
    server = MinecraftServer.lookup(servidor)
    print("Searching and checking server")
    try:
        status = server.status()
        await ctx.send('El servidor está abierto con {} jugadores y un ping de {} ms'.format(status.players.online, round(status.latency)))
    except:
        await ctx.send('El servidor está cerrado')


@bot.event
async def on_ready():
    game = discord.Game('!setup to start')
    await bot.change_presence(activity=game)



bot.run(yourtoken)
