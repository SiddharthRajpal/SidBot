import discord
from discord.ext import commands
from discord import embeds
import os
from keep_alive import keep_alive
import asyncio
from email.message import EmailMessage
import smtplib



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
async def _8ball(ctx, *, question= None):

  responses = [
  "As I see it, yes.", 
  "Ask again later.", 
  "Better not tell you now.", 
  "Concentrate and ask again.",
  "Don’t count on it.", 
  "It is certain.", 
  "It is decidedly so.", 
  "Most likely.", 
  "My reply is no.", 
  "No",
  "d"
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
  em = discord.Embed(title = "8ball Answer" , color= discord.Color.dark_gold())
  em.add_field(name = "Question", value = question)
  em.add_field(name = "Answer",value = random.choice(responses))
  await ctx.channel.send(embed = em)
    
  
@root.command()
async def help(ctx):
  hi = discord.Embed(title = "SidBBot by RandomPotato", description = "Welcome to this message. SidBot is a custom bot that I have built specifically for this server using python. I will tell you about the commands and uses of SidBot",color=discord.Color.green())
  
  hi.add_field(name = ".src", value = "view link for the source code")
  hi.add_field(name = ".help", value = "Get help")
  hi.add_field(name = ".ping",value = "Sends the current ping (latency)")
  hi.add_field(name = ".8ball <question>",value = "Ask a Question")
  hi.add_field(name = ".spam <message>",value = "Spam Stuff")
  hi.add_field(name = ".stopspam",value="Stops Spamming")
  hi.add_field(name = ".clear <amount>", value = "clears number of messages specified")
  hi.add_field(name = ".say <stuff>", value = "says stuff")
  hi.add_field(name = ".email <receiver> <subject> <message>", value = "Send an email to someone right within discord!!!!")
  await ctx.channel.send(embed = hi)
  
@root.command()
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f"Deleted {amount} Messages :)")


@root.command()
async def say(ctx, *,message):
  em = discord.Embed(color = discord.Color.red())
  em.add_field(name = message , value = f"- {ctx.author.name}")
  await ctx.channel.send(embed = em)
  
@root.command()
async def email(ctx, receiver, subject, *, mail):
  try:
    msg = EmailMessage()
    msg.set_content(mail)
    msg['Subject'] = subject
    msg['From'] = "sidotpconfirmation@gmail.com"
    msg['To'] = receiver
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("sidotpconfirmation@gmail.com", "Blocked For Privacy Reasons")
    server.send_message(msg)
    server.quit()
  except:
      await ctx.channel.send('Error in sending email, pls use the correct format <receiver> <subject> <message>')

keep_alive()
my_secret = os.environ['key']
root.run(my_secret)
