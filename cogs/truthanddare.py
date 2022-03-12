import discord
import os
import aiohttp
from discord.ext import commands
from discord.ext.commands import BucketType
import random


class td(commands.Cog):
    def _init__(self,client):
        self.client=client
    
    @commands.command()
    async def Truth_or_Dare(self,ctx,message):
        if message=="Truth":
            responses=["When was the last time you lied?",
                    "When was the last time you cried?",
                    "What's your biggest fear?",
                    "What's your biggest fantasy?",
                    "Do you have any fetishes?",
                    "What's something you're glad your mum doesn't know about you?",
                    "Have you ever cheated on someone?",
                    "What's the worst thing you've ever done?",
                    "What's a secret you've never told anyone?",
                    "Do you have a hidden talent?",
                    "Who was your first celebrity crush?",
                    "What are your thoughts on polyamory?",
                    "What's the worst intimate experience you've ever had?",
                    "Have you ever cheated in an exam?",
                    "What's the most drunk you've ever been?",
                    "Have you ever broken the law?",
                    "What's the most embarrassing thing you've ever done?",
                    "What's your biggest insecurity?",
                    "What's the biggest mistake you've ever made?",
                    "What's the most disgusting thing you've ever done?",
                    "What's the worst thing anyone's ever done to you?",
                    "Have you ever had a run in with the law?",
                    "What's your worst habit?",
                    "What's the worst thing you've ever said to anyone?",
                    "Have you ever peed in the shower?",
                    "What's the strangest dream you've had?"
                    ]
            await ctx.send(f"{random.choice(responses)}")
        elif message=="Dare":
            responses= ["Show the most embarrassing photo on your phone",
                        "Show the most embarrassing photo on your phone",
                        "Show the last five people you texted and what the messages said",
                        "Let the rest of the group DM someone from your Instagram account",
                        "Eat a raw piece of garlic",
                        "Do 100 squats",
                        "Keep three ice cubes in your mouth until they melt",
                        "Say something dirty to the person on your left",
                        "Give a foot massage to the person on your right",
                        "Put 10 different available liquids into a cup and drink it",
                        "Yell out the first word that comes to your mind",
                        "Like the first 15 posts on your Facebook newsfeed",
                        "Keep your eyes closed until it's your go again",
                        "Empty out your wallet/purse and show everyone what's inside",
                        "Pretend to be the person to your right for 10 minutes",
                        "Eat a snack without using your hands",
                        "Say two honest things about everyone else in the group",
                        "Try and make the group laugh as quickly as possible",
                        "Try to put your whole fist in your mouth",
                        "Tell everyone an embarrassing story about yourself",
                        "Try to lick your elbow",
                        "Post the oldest selfie on your phone on Instagram Stories"
                    ]
            await ctx.send(f"{random.choice(responses)}")
        else:
            await ctx.send("Chose a valid option")

    @commands.command()
    async def task_completed(self,ctx):
        await ctx.send(f"{ctx.author.mention}, Your task is complete" )
        await ctx.send("https://imgflip.com/s/meme/Leonardo-Dicaprio-Cheers.jpg")

    @commands.command()
    async def task_incomplete(self,ctx):
        await ctx.send(f"{ctx.author.mention}, You could not complete your task" )
        await ctx.send("https://i.imgflip.com/1o12mo.jpg")


    
def setup(client):
    client.add_cog(td(client))