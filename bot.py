import discord
from discord.ext import commands
import os
import pymongo

Mongo=open("mongodb.txt","r").readline()
TOKEN = open("token.txt", "r").readline()


clientmongo = pymongo.MongoClient(Mongo)
db = clientmongo.test

intents = discord.Intents().all()
client=commands.Bot(command_prefix="_",intents=intents,help_command=None)

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def load(ctx,extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx,extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        


@client.command()
async def hello(ctx,text="Say something dumbass"):
    await ctx.send(text)


@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(
    colour = discord.Colour.green())
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_author(name = 'Help : list of commands available')
    embed.add_field(name = '_info', value = 'Gives info about the pksbot', inline = False)
    embed.add_field(name = '_all', value = 'List of all commands', inline = False)
    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def all(ctx):
    embed = discord.Embed(
    colour = discord.Colour.red())
    embed.set_author(name = 'All commands of PAPBot')
    embed.add_field(name = '_hello', value = 'Says hello to the tagged member', inline = False)
    embed.add_field(name = '_cgpacalc', value = 'Calculates your CGPA (pass Grade Score,Grade Score)', inline = False)
    embed.add_field(name = '_showgpa', value = 'Returns your CGPA', inline = False)
    embed.add_field(name = '_target', value = 'Tells you how much you need to score to achieve target(pass targetgpa,credits of next sem)', inline = False)
    embed.add_field(name = '_updategpa', value = 'Updates your GPA (pass Grade Score,Grade Score)', inline = False)
    embed.add_field(name = '_work', value = 'Starts the Pomodoro Timer', inline = False)
    embed.add_field(name = '_takebreak', value = 'Starts the Break Timer', inline = False)
    embed.add_field(name = '_add', value = 'Adds a task to your To-Do List', inline = False)
    embed.add_field(name = '_done', value = 'Removes the completed task and updates your To-Do List', inline = False)
    embed.add_field(name = '_show', value = 'Shows your current To-Do List', inline = False)
    embed.add_field(name = '_add_deadline', value = 'Adds a Deadline', inline = False)
    embed.add_field(name = '_remove_deadline', value = 'Removes a Deadline', inline = False)
    embed.add_field(name = '_print_deadline', value = 'Prints information about your Deadline', inline = False)
    embed.add_field(name = '_ball', value = 'Random game', inline = False)
    embed.add_field(name = '_PAPbot', value = 'With love PAP', inline = False)
    embed.add_field(name = '_poll', value = 'Helps create poll', inline = False)
    embed.add_field(name = '_add_deadline', value = 'Adds a Deadline', inline = False)
    embed.add_field(name = '_snl', value = 'Initiates the snake & ladder game', inline = False)
    embed.add_field(name = '_move', value = 'Moves players position on the SNL board', inline = False)
    embed.add_field(name = '_killsnl', value = 'Terminates Snakes and Ladders game', inline = False)
    embed.add_field(name = '_tictactoe', value = 'Initiates TicTacToe game', inline = False)
    embed.add_field(name = '_killgame', value = 'Terminates TicTacToe game', inline = False)
    embed.add_field(name = '_Truth_or_Dare', value = 'Displays either a truth question or a dare', inline = False)
    embed.add_field(name = '_task_completed', value = 'Displays your task completion status', inline = False)
    embed.add_field(name = '_task_incomplete', value = 'Displays your task incompletion status', inline = False)

    
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
    colour = discord.Colour.purple())    
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_author(name = 'Information')
    embed.add_field(name = 'What is it?', value = 'PAPbot is a discord bot made using `python`', inline = False)
    embed.add_field(name = 'Hosting', value = 'Hosted on Heroku, currently in development stage', inline = False)
    embed.add_field(name = 'Author', value = 'Made by `PAP`', inline = False)
    await ctx.send(embed = embed)



client.run(TOKEN)
