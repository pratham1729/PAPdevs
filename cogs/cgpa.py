import discord
from discord.ext import commands
import os
import pymongo

clientmongo = pymongo.MongoClient("mongodb+srv://pratham1729:fazR7URJuvdXtKH@cluster0.jc0rc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = clientmongo.test


class cog1(commands.Cog):
    def __init__(self,client):
        self.client=client


    @commands.command()
    async def cgpacalc(self,ctx, *,string):
        y=ctx.message.guild.name
        y=y.replace(" ","_")
        x=ctx.message.author
        u=ctx.message.author.id
        string=string.split(",")
        grades=[]
        credits=[]
        cgpa=0
        for i in string:
            a,b=tuple(map(int,i.split()))
            grades.append(b)
            credits.append(a)
            cgpa+=a*b
        credits=sum(credits)
        cgpa=cgpa/credits
        await ctx.send(f"{x.mention} your CGPA is {cgpa}")
        x=str(x)
        db=clientmongo[y]
        col=db["GPA"]
        y=col.find({"name":x})
        c=0
        for i in y:
            c+=1
        if c==1:
            myquery={"_id":u}
            newval={"$set":{"cgpa":cgpa,"credits":credits}}
            col.update_one(myquery, newval)
        else:
            dic={"_id":u,"name":x,"cgpa":cgpa,"credits":credits}
            x = col.insert_one(dic)

    @commands.command()
    async def showgpa(self,ctx):
        x=ctx.message.author
        u=ctx.message.author.id
        y=str(x)
        mydb=str(ctx.message.guild.name)
        mydb=mydb.replace(" ","_")
        db=clientmongo[mydb]
        col=db["GPA"]
        p=col.find_one({"_id":u})
        q=p
        c=0
        for i in p:
            c+=1
        if c==0:
            await ctx.send(f"Sorry {x.mention}, no record found, please create one")
        else:
            t=q["cgpa"]
            await ctx.send(f"{x.mention}, your GPA is {t}") 

    @commands.command()
    async def target(sself,ctx,string):
        a=string.split(",")
        tgt=float(a[0])
        cred=int(a[1])
        x=ctx.message.author
        u=ctx.message.author.id
        y=str(x)
        mydb=str(ctx.message.guild.name)
        mydb=mydb.replace(" ","_")
        db=clientmongo[mydb]
        col=db["GPA"]
        p=col.find_one({"_id":u})
        q=p
        c=0
        for i in p:
            c+=1
        if c==0:
            await ctx.send(f"{x.mention}, no record found")
        else:
            t=(((q["credits"]+cred)*tgt)-(q["credits"]*q["cgpa"]))/cred
            if t>10:
                await ctx.send(f"{x.mention}, sorry your target is unachievable")
            else:    
                await ctx.send(f"{x.mention}, you'll need atleast {t} in your next sem for your target")

    @commands.command()
    async def updategpa(self,ctx, *,string):
        x=ctx.message.author
        u=ctx.message.author.id
        y=str(x)
        mydb=str(ctx.message.guild.name)
        mydb=mydb.replace(" ","_")
        db=clientmongo[mydb]
        col=db["GPA"]
        string=string.split(",")
        grades=[]
        credits=[]
        cgpa=0
        for i in string:
            a,b=tuple(map(int,i.split()))
            grades.append(b)
            credits.append(a)
            cgpa+=a*b
        credits=sum(credits)
        cgpa=cgpa/credits
        p=col.find_one({"_id":u})
        q=p
        c=0
        for i in p:
            c+=1
        if c==0:
            k=col.insert_one({"_id":u,"name":y,"cgpa":cgpa,"credits":credits})
            await ctx.send(f"{x.mention}, your new GPA is {cgpa}") 
        else:
            temp=(q["cgpa"]*q["credits"]+credits*cgpa)/(credits+q["credits"])
            oldval={"_id":u}
            newval={"$set":{"cgpa":temp,"credits":q["credits"]+credits}}
            col.update_one(oldval,newval)
            await ctx.send(f"{x.mention}, your new GPA is {temp}") 

def setup(client):
    client.add_cog(cog1(client))