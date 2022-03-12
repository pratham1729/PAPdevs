from itertools import count
from urllib.parse import parse_qsl
import discord
from discord.ext import commands
client= commands.Bot(command_prefix=',')
@client.command()   
async def PAPbot(ctx):
        channel=ctx.channel
        txt=f'Made with love - PAP (Pratham | Arshita | Pradnya)'
        embed=discord.Embed(title='PAPdevs',description=txt,colour=discord.Colour.red())
        emoji1 = '\N{White Heart}'
       
        

        message=await channel.send(embed=embed)
        await message.add_reaction(emoji1)
        

       
        
client.run('OTUxNDI4NzEyMDY5NDcyMjc3.YinVCQ.ErzMNl7XppzZkimKf215TXKGRXs')
