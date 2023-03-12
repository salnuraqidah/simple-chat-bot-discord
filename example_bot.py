
# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

# client = discord.Client(intents=intents)

client = commands.Bot(
    command_prefix="!",
    intents=intents,
)

TOKEN = 'MTA4MzczMzA5MjU3NDk2OTkxNg.GVuWD1.QhZUi0Gl4asPmsgfDec8PtMsjeRAM7vRpeZ4FU'
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.command()
async def hello(ctx):
  await ctx.send("Hiii")

@client.command(name='coloured_text')
async def test(ctx): 
    retStr = str("""```yaml\nThis is some colored Text```""") 
    await ctx.send(retStr)
    
@client.event
async def on_member_join(member):
  channel = client.get_channel(1083732775011631146)
  await channel.send(f'Hi {member.name}, welcome to SAL server!')
  
@client.event
async def on_member_remove(member):
  channel = client.get_channel(1083732775011631146)
  await channel.send(f'Goodbye {member.name}!')

@client.command(name='now')
async def jamberapa(ctx):
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  await ctx.send(dt_string)
  
client.run(TOKEN)

