import discord
import os
from discord.ext import commands


client=commands.Bot(command_prefix=".")

@client.command()
async def load(ctx,extension):
    client.load_extension(f"cogs.{extension}")


client.run('OTUxODcyMDE2NDUyMDMwNDk2.Yitx5Q.LiiQsoNU1XA0R7238tsmqs9wp0U')