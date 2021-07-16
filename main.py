import discord
from discord.ext import commands
from discord import embeds
import os
from keep_alive import keep_alive
import asyncio

from replit import db
import random
command_prefix = "."
root = commands.Bot(command_prefix = command_prefix, help_command = None)


mutelist = []
bad_words = [
  "kutta",
  "kamina"
]
db["y"] = False
youtube_id = "UCoZXfoF3r-uB_uhWWPP2cJw"
@root.event
async def on_ready():
  print("Ready")
  await root.change_presence(activity=discord.Game(name=" .help"))

@root.command()
async def ping(ctx):
  await ctx.channel.send(f"{round(root.latency * 1000)} MS")


@root.command()
async def src(ctx):
  await ctx.channel.send("Source code available on github :- https://github.com/SiddharthRajpal/SidBot")

@root.command()
async def spam(ctx,*,message):
  db["y"] = True
  while db["y"]:
    await ctx.send(message)

@root.command()
async def stopspam(ctx):
  db["y"] = False
  await ctx.send("Stopped All Spams")




@root.command(aliases = ['8ball'])
async def _8ball(ctx, *, question="None"):

  responses = [
  "As I see it, yes.", 
  "Ask again later.", 
  "Better not tell you now.", 
  "Cannot predict now.", 
  "Concentrate and ask again.",
  "Don’t count on it.", 
  "It is certain.", 
  "It is decidedly so.", 
  "Most likely.", 
  "My reply is no.", 
  "No",
  ""
  "My sources say no.",
  "Outlook not so good.", 
  "Outlook good.", 
  "Reply hazy, try again.", 
  "Signs point to yes.",
  "Very doubtful.", 
  "Without a doubt.",
  "Yes.", 
  "Yes – definitely.", 
  "You may rely on it."]
  await ctx.channel.send(f"```Question :- {question} \nAnswer :- {random.choice(responses)}``` ")


@root.command()
async def help(ctx):
  await ctx.channel.send(
      """         ```           SidBot BY RandomPotato
Welcome to this message. SidBot is a custom bot that I have built specifically for this server using python. I will tell you about the commands and uses of SidBot


.src :- view link for the source code
.help :- Get help
.8ball :- Ask a Question
.spam :- Spam Stuff
.stopspam :- Stop Spamming
If there are any suggestions or queries or bugs please feel free to DM me :)```""")








keep_alive()
root.run("ODY1NjU5ODQzNTk1MzM3NzQ4.YPHOjQ.TA0KoZ-g-CwsjXypUrJBK_9CqNI")
