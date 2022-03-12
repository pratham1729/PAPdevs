import discord
from discord.ext import commands
import asyncio
import io




class cog5(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()   
    async def work(self,ctx,time):
            minutes,seconds=tuple(map(int,time.split(":")))
            minuteint=minutes
            if seconds>60:
                minuteint=minuteint+int(seconds/60)
                seconds=seconds-int(seconds/60)*60
            if minuteint < 0:
                await ctx.send('```Use your brain , seriously!```')
                raise BaseException
            message = await ctx.send(f'```Work : {minutes} : {seconds}```')
            if seconds!= 0:
                for secondint in range(seconds,0,-1):
                        await message.edit(content=f'```Work : {minuteint} : {secondint}```')
                        await asyncio.sleep(1)         
            while minuteint>0:
                    minuteint -=1
                    for secondint in range(60,0,-1):
                        await message.edit(content=f'```Work : {minuteint} : {secondint}```')
                        await asyncio.sleep(1)

            
            await message.edit(content='```Your Pomodoro Work Session Ended```')
    
            await ctx.send("https://images.rawpixel.com/image_400/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0yNTRiYXRjaDItZmluYWwtMDkuanBn.jpg?s=rRci4mxvojI1j5KHbJc5GbdDIi1rpzCB2kdaM40UwEM")
            await ctx.send(f'{ctx.author.mention},```Work Session Ended```')
            await ctx.send("https://pbs.twimg.com/media/ENBYDiNW4AA0kpm.jpg")
            await ctx.send(f'```To take break use "takebreak" command```')

    @commands.command()   
    async def takebreak(self,ctx,time):
            minutes,seconds=tuple(map(int,time.split(":")))
            minuteint=minutes
            if seconds>60:
                minuteint=minuteint+int(seconds/60)
                seconds=seconds-int(seconds/60)*60
            if minuteint < 0:
                await ctx.send('```Use your brain , seriously!```')
                raise BaseException
            message = await ctx.send(f'```Break : {minutes} : {seconds}```')
            if seconds!= 0:
                for secondint in range(seconds,0,-1):
                        await message.edit(content=f'```Break : {minuteint} : {secondint}```')
                        await asyncio.sleep(1)         
            while minuteint>0:
                    minuteint -=1
                    for secondint in range(60,0,-1):
                        await message.edit(content=f'```Break : {minuteint} : {secondint}```')
                        await asyncio.sleep(1)

            
            await message.edit(content='```Your Pomodoro break Session Ended```')
    

            await ctx.send(f'{ctx.author.mention},```Break Session Ended```')
            await ctx.send("https://syedbalkhi.com/wp-content/uploads/2015/09/timetostart.jpg")
            await ctx.send(f'```To start work use "work" command```')

def setup(client):
    client.add_cog(cog5(client))