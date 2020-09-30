import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
try:
    from bs4 import BeautifulSoup
    hasSoup = True
except:
    hasSoup = False

class mtgUtility:
    """Utility Functions for Magic the Gathering"""

    #Discord Commands


    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    if hasSoup:
        bot.add_cog(mtgUtility(bot))
    else:
        print("Install BeautifulSoup4 using pip install BeautifulSoup4")

#Utility Classes
class mtgCard:

    def __init__(self, url: str):
        self.url = url
        scrape(self.url)


    def scrape(url: str):
        
