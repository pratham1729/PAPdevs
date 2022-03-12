import discord
from discord.ext import commands

class cogx(commands.Cog):
    def __init__(self,client):
        self.client=client

    

    @commands.command()   
    async def PAPbot(self,ctx):
            channel=ctx.channel
            txt=f'Made with love - PAP (Pratham | Arshita | Pradnya)'
            embed=discord.Embed(title='PAPdevs',description=txt,colour=discord.Colour.red())
            emoji1 = '\N{White Heart}'
        
            

            message=await channel.send(embed=embed)
            await message.add_reaction(emoji1)
def setup(client):
    client.add_cog(cogx(client))
       
        
