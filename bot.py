import discord
import os

from cogs.cat import CatFact
# creates bot instance
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# intents are like "intentions" for granting access - you can set T(enable)/F(disable)
intents = discord.Intents.all()  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('--------------------------------------------')
    print(f'{bot.user.name} - has connected to Discord!')
    await bot.add_cog(CatFact(bot))

if __name__ == "__main__" :
    bot.run(TOKEN)


