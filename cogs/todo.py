import discord
from discord.ext import commands
import os
import pymongo


clientmongo = pymongo.MongoClient("mongodb+srv://pratham1729:fazR7URJuvdXtKH@cluster0.jc0rc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = clientmongo.test


class cog2(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def add(self,ctx, *,task):
        y=ctx.guild.name
        x=ctx.message.author.id
        y=y.replace(" ","_")
        db=clientmongo[y]
        col=db["todo"]
        p=col.find_one({"_id":x})
 
        if p==None:
            dic={"_id":x,"tasks":[task],"name":str(self.client.get_user(x))}
            col.insert_one(dic)
        else:
            l=p["tasks"]
            l.append(task)
            oldval={"_id":x}
            newval={"$set":{"tasks":l,"name":str(self.client.get_user(x))}}
            col.update_one(oldval,newval)
        await ctx.send('Task Added')   

    @commands.command()
    async def show(self,ctx):        
        y=ctx.message.guild.name
        x=ctx.message.author.id
        y=y.replace(" ","_")
        db=clientmongo[y]
        col=db["todo"]
        p=col.find_one({"_id":x})
        l=p["tasks"]
        embed = discord.Embed(
        colour = discord.Colour.orange())
        embed.set_author(name = f"{self.client.get_user(x)}'s To-Do list")
        for i in range(len(l)):    
            embed.add_field(name=f"{i+1}",value = f"{l[i]}",inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)       
        await ctx.send(embed = embed)


    
    @commands.command()
    async def done(self,ctx,num):
        y=ctx.message.guild.name
        x=ctx.message.author.id
        num=int(num)
        y=y.replace(" ","_")
        db=clientmongo[y]
        col=db["todo"]
        p=col.find_one({"_id":x})
        l=p["tasks"]
        del(l[num-1])
        oldval={"_id":x}
        newval={"$set":{"tasks":l}}
        col.update_one(oldval,newval)

def setup(client):
    client.add_cog(cog2(client))