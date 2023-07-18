from discord.ext import commands
import requests

# Cog - big picture of all the "bots" you can run
class CatFact(commands.Cog):

    # have to use await -- nothing else can happen while I'm waiting for this call to finish
    @commands.command(help="This command sends a cat fact to the channel when requested")
    async def catfact(self, ctx):
        r = requests.get('https://catfact.ninja/fact')
        print("r.json is ", r.json())
        
        await ctx.send(r.json()['fact'])

    @commands.command(help="This command sends a random cat picture to the channel when requested")
    async def catpic(self, ctx):
        # TO DO: Sends a cat picture into the chat
        await ctx.send("~WIP~")