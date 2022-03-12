import discord
from discord.ext import commands
import os
import pymongo





clientmongo = pymongo.MongoClient("mongodb+srv://pratham1729:fazR7URJuvdXtKH@cluster0.jc0rc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
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
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount+1) #as it will count our .clear as one command

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')

@client.command()
async def ban(ctx,member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def hello(ctx,text="Say something dumbass"):
    await ctx.send(text)

@client.command()
async def unban(ctx,* ,member):
    banned_users=await ctx.guild.bans()
    member_name,member_discriminator=member.split("#")

    for banned_entry in banned_users:
        user=banned_entry.user
        if(user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


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
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_author(name = 'All commands of PKSBot')
    embed.add_field(name = '_clear', value = 'Clears the chat upto a number provided', inline = False)
    embed.add_field(name = '_hello', value = 'Says hello to the tagged member', inline = False)
    embed.add_field(name = '_cgpacalc', value = 'Calculates your cgpa (pass Grade Score,Grade Score....)', inline = False)
    embed.add_field(name = '_showgpa', value = 'Returns your cgpa', inline = False)
    embed.add_field(name = '_target', value = 'Tells you how much you need to score to achieve target(pass targetgpa,credits of next sem)', inline = False)
    embed.add_field(name = '_updategpa', value = 'Updates your gpa (pass Grade Score,Grade Score....)', inline = False)
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
    colour = discord.Colour.purple())    
    embed.set_thumbnail(url= client.user.avatar_url)
    embed.set_author(name = 'Information')
    embed.add_field(name = 'What is it?', value = 'pksbot is a discord bot made using `python` for cgpa management', inline = False)
    embed.add_field(name = 'Hosting', value = 'Hosted on Heroku, currently in development stage', inline = False)
    embed.add_field(name = 'Author', value = 'Made by `PAP`', inline = False)
    await ctx.send(embed = embed)



client.run("OTM3MzE2Mzg4MzU4NDU5NDAz.YfZ96Q.5tpsWCsBT_ZegMahF2kBv0mR0qo")