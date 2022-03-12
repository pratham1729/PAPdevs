import discord
import random
import json
from discord.ext import commands
from discord_components import *
from asyncio import sleep as s
import pymongo
Mongo=open("mongodb.txt","r").readline()
clientmongo = pymongo.MongoClient(Mongo)
db = clientmongo.test


y=""

def get_deadline(client,message):
    with open("deadline.json","r")as f:
        deadlines=json.load(f)
    return deadlines[str(message.guild.id)]

sub={}
dead={}
hour={}

class cog4(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        with open("deadline.json","r") as f:
            deadlines=json.load(f)
        
        deadlines[str(guild.id)] = "Add your deadlines"

        with open("deadline.json","w")as f:
            json.dump(deadlines, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        with open("deadline.json","r")as f:
            deadlines=json.load(f)

        deadlines.pop(str(guild.id))

        with open("deadline.json","w")as f:
            json.dump(deadlines, f, indent=4)

    @commands.command()
    async def add_deadline(self,ctx,*,string):
        string=string.split()
        x=int(string[0])
        subject=string[1]
        deadline=int(string[2])
        hours=int(string[3])
        with open("deadline.json","r")as f:
            deadlines=json.load(f)
        
        deadlines[str(ctx.guild.id)]=deadline
        sub[x]=subject
        dead[x]=deadline
        hour[x]=hours
        await ctx.send(f"Your deadline of {subject} is in {deadline} minutes and {hours} seconds ")
        
        with open("deadline.json","w")as f:
            json.dump(deadlines, f, indent=4)
        
        while True:
            await s((deadline*60)+(hours)-60)
            await ctx.send("https://images.news18.com/ibnlive/uploads/2022/02/ashneer-grover-2-16455906144x3.png")
            await ctx.send(f"{ctx.author.mention} deadline is in 1 minute. Hurry up!")
            break
        while True:
            await s((deadline*60)+(hours))
            await ctx.send("https://www.scrolldroll.com/wp-content/uploads/2021/09/khatam-tata-good-bye-rahul-gandhi-meme-template.jpg")
            await ctx.send(f"{ctx.author.mention} deadline is past due.")
            break

    @commands.command()
    async def remove_deadline(self,ctx,a: int):
        del sub[a]
        del dead[a]
        del hour[a]
        

        await ctx.send("https://image.shutterstock.com/image-vector/well-done-colorful-typography-banner-260nw-1356737636.jpg")
        

    @commands.command()
    async def print_deadline(self,ctx):
        for k, v in sub.items():
            subject=v
            await ctx.send("{:<8} {:<15}".format(k, subject))

    
    """@client.command()
    async def remove_deadline(ctx,x):
        
        await ctx.send("https://image.shutterstock.com/image-vector/well-done-colorful-typography-banner-260nw-1356737636.jpg")
        with open("deadline.json","r")as f:
            deadlines=json.load(f)
        sub.pop(x-1)
        dead.pop(x-1)
        hour.pop(x-1)
        
        deadlines.pop(str(ctx.guild.id))
        
        with open("deadline.json","w")as f:
            json.dump(deadlines, f, indent=4)"""

        





    """@client.command()
    async def print_deadlines(ctx,time): minutes,seconds=tuple(map(int,time.split(":")))
        
            minuteint=dead[x]
            if seconds>60:
            minuteint=minuteint+int(seconds/60)
            seconds=seconds-int(seconds/60)*60
            if minuteint < 0:
            await ctx.send('Use your brain , seriously!')
            raise BaseException
            message = await ctx.send(f'Time Left : {minutes} : {seconds}')
            if seconds!= 0:
                for secondint in range(seconds,0,-1):
                        await message.edit(content=f'Time Left : {minuteint} : {secondint}')
                        await asyncio.sleep(1)
            while minuteint>0:
                    minuteint -=1
                    for secondint in range(60,0,-1):
                        await message.edit(content=f'Time Left : {minuteint} : {secondint}')
                        await asyncio.sleep(1)
    
        for x in range(len(sub)):
        
            message=await ctx.send(f'Time left: {dead[x]}:{hour[x]}')
            await ctx.send(f"{x+1}: The deadline for {sub[x]} is in {dead[x]} days and {hour[x]} hours ")
            while dead[x]>0:
                dead[x]-=1
                for hourint in range(hour[x],0,-1):
                    for minuteint in range(60,0,-1):
                        for secondint in range(60,0,-1):
                            
                            await message.edit(content=f'Work : {dead[x]} : {hour[x]} : {minuteint}')
                            await asyncio.sleep(1)"""
                        

    @commands.command(aliases=["8ball","test"])
    async def ball(self,ctx, *,question):
        y=ctx.guild.name
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
                    ]
        await ctx.send(random.choice(responses))
def setup(client):
    client.add_cog(cog4(client))

    
