import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event #it defines an event handler that is triggered when the bot is ready and logged in
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command() #it defines the command "hello" that sends a greeting message when invoked
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command() #it defines the command "heh" that takes an optional integer argument "count_heh" with a default value of 5
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command() #it defines the command "choose" that takes a string of options separated by commas
async def choose(ctx, *, opciones): 
    opciones = opciones.split(",") 
    respuesta = random.choice(opciones)

    await ctx.send("He elegido: " + respuesta)

@bot.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `discord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `discord.User` instance.
    # The documentation notes what can be converted, in the case of `discord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 80088516616269824, @Danny or Danny#0007

    # Note: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `discord.User` instance
    # and can do the following:
    user_id = user.id
    username = user.name
    avatar = user.display_avatar.url
    await ctx.send(f'User found: {user_id} -- {username}\n{avatar}')


bot.run("Secret Token")
