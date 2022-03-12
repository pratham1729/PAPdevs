from itertools import count
from urllib.parse import parse_qsl
import discord
from discord.ext import commands

class poll(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()   
    async def poll(self,ctx,p1:discord.Member,p2:discord.Member,*,question,):
            channel=ctx.channel
            txt=f'{question}\nReact with 🟨 for choice 1 : '+"<@"+str(p1.id)+'> or 🟩 for choice 2 : '+"<@"+str(p2.id)+'>'
            embed=discord.Embed(title='Poll',description=txt,colour=discord.Colour.red())
            emoji1 ='\N{Large Yellow Square}'
            emoji2 ='\N{Large Green Square}'
            message=await channel.send(embed=embed)
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
def setup(client):
    client.add_cog(poll(client))
        
            

