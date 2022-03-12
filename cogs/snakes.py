import discord
from discord.ext import commands
import random

player1=""
player2=""
turn=""
p1=0
p2=0
gameOver=True
board=[]
snake={45:6,60:19,77:17,87:37,89:11,94:69,99:9}
ladder={7:26,16:39,13:55,40:78,44:76,47:68,49:91,61:96}
class cog6(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def snl(self,ctx,plr1:discord.Member,plr2:discord.Member):
        global player1
        global player2
        global turn
        global gameOver
        global p1
        global p2
        player1=plr1
        player2=plr2
        if gameOver:
            global board
            board=[":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:"]
            turn=""
            gameOver=False
            line=""
            
            print(len(board))
            for x in range(len(board)):
                if x in (9,19,29,39,49,59,69,79,89,99):
                    line += " "+board[x]
                    await ctx.send(line)
                    line=""
                else:
                    line += " "+board[x]

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
    async def move(self,ctx):

        pos=random.randint(1,6)
        global turn
        global player1
        global player2
        global p1
        global p2
        global board
        global gameOver

        if not gameOver:
            mark=""
            if turn == ctx.author:
                if turn == player1:
                    if p1!=0:    
                        board[p1-1]=":white_large_square:"
                        board[p2-1]=":blue_circle:"
                    mark=":red_circle:"
                    p1=p1+pos
                    if p1 in snake.keys():
                        p1=snake[p1]
                    if p1 in ladder.keys():
                        p1=ladder[p1]
                    board[p1-1]=mark

                elif turn == player2:
                    mark=":blue_circle:"
                    if p2!=0:
                        board[p2-1]=":white_large_square:"
                        board[p1-1]=":red_circle:"
                    p2=p2+pos
                    if p2 in snake.keys():
                        p2=snake[p1]
                    if p2 in ladder.keys():
                        p2=ladder[p1]
                    board[p2-1]=mark

                if p1==p2:
                    board[p1-1]=":people_hugging:"

                line=""
            
                for x in range(len(board)):
                    if x in (9,19,29,39,49,59,69,79,89,99):
                        line += " "+board[x]
                        await ctx.send(line)
                        line=""
                    else:
                        line += " "+board[x]
                if p1>=100:
                    gameOver=True
                elif p2>=100:
                    gameOver=True

                if gameOver:
                        await ctx.send(f'```{turn},won!!```')
                if turn==player2: 
                            turn=player1
                elif turn==player1:
                            turn=player2

            else:
                await ctx.send("```Not your turn huh!```")
        else:
            await ctx.send("```Please start a new game using snakes and ladder command.```")


def setup(client):
    client.add_cog(cog6(client))