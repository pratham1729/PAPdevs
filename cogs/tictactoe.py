from itertools import count
from urllib.parse import parse_qsl
import discord
import random
from discord.ext import commands
player1=""
player2=""
turn=""
gameOver=True
board= []
def checkWinner(winningConditions,mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]]==mark and board[condition[1]]==mark and board[condition[2]]==mark:
                gameOver=True
def strcomp(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        else:
            return True
class cog3(commands.Cog):
    def __init__(self,client):
        self.client=client

    winningConditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    @commands.command()
    async def killgame(self,ctx):
        global gameOver
        gameOver=True
        await ctx.send(f"{ctx.message.author.mention} ended the game")
    @commands.command()
    async def tictactoe(self,ctx,p1:discord.Member,p2:discord.Member):
        global player1
        global player2
        global turn
        global gameOver
        global count
        
        if gameOver:
            global board
            board=[":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:"]
            turn=""
            gameOver=False
            count=0

            player1=p1
            player2=p2
            line=""
            embed = discord.Embed(
            colour = discord.Colour.orange())
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " "+board[x]
                    line+="\n"
                else:
                    line += " "+board[x]
            embed.add_field(name="Board",value = f"{line}",inline=False)
            await ctx.send(embed=embed)
            num=random.randint(1,2)
            if num==1:
                turn = player1
                await ctx.send("<@"+str(player1.id)+'>your turn')
            elif num == 2:
                turn = player2
                await ctx.send("<@"+str(player2.id)+'>your turn')
        else:
            await ctx.send("```A game is already in progress. Finish it before starting a new one.```")

    @commands.command()
    async def place(self,ctx, pos):
        pos=int(pos)
        global turn
        global player1
        global player2
        global board
        global count
        if not gameOver:
            mark=""
            if turn == ctx.author:
                if turn == player1:
                    mark=":regional_indicator_x:"
                elif turn == player2:
                    mark=":o2:"

                if (0 < pos) and (pos < 10) and (strcomp(board[pos-1],":white_large_square:")):

                    board[pos-1]= mark
                    count+=1
                    line=""
                    embed = discord.Embed(
                    colour = discord.Colour.orange())
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " "+board[x]
                            line+="\n"
                        else:
                            line += " "+board[x]
                    embed.add_field(name="Board",value = f"{line}",inline=False)
                    await ctx.send(embed=embed)
                    checkWinner(self.winningConditions,mark)
                    if gameOver:
                            await ctx.send(f'```{turn},won!!```')
                    elif count >= 9:
                            await ctx.send(f'```Tie!!```')
                    if turn==player2: 
                            turn=player1
                    elif turn==player1:
                            turn=player2
                else:
                    await ctx.send('```Use integer between 1 & 9 and an unmarked space```')
            else:
                await ctx.send("```Not your turn huh!```")
        else:
            await ctx.send("```Please start a new game using tictactoe command.```")

    @tictactoe.error
    async def tictactoe_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('```Please mention two players```')
        elif isinstance(error,commands.BadArgument):
            await ctx.send('```Please ping player```')

    @place.error
    async def place_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('```Please enter the position```')
        elif isinstance(error,commands.BadArgument):
            await ctx.send('```Please input an integer```')

def setup(client):
    client.add_cog(cog3(client))
