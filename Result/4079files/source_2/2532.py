import discord
from discord.ext import commands
from .utils import checks
import urllib
import urllib.request
import shutil
import zipfile
import os
from .utils.dataIO import dataIO
try:
    import PIL
    from PIL import ImageFont
    from PIL import Image
    from PIL import ImageDraw
    hasPil = True
except:
    hasPil = False

from datetime import datetime

class waitingTitan:
    """Functions for Waking Titan ARG"""

    def __init__(self, bot):
        self.file_path = "data/waitingTitan/Data.json"
        self.json_data = dataIO.load_json(self.file_path)
        self.bot = bot


    @commands.group(name="waiting", pass_context=True)
    @checks.mod_or_permissions(manage_server=True)
    async def _waiting(self, ctx):
        """Waiting Tasks for WakingTitan"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_waiting.command(pass_context = True)
    async def image(self, ctx):
        """Generates a Reminder Image stating that when last something might have happened"""
        image = createImage()
        image.save('data/waitingTitan/temp.png')
        channel = ctx.message.channel
        await self.bot.send_file(channel, 'data/waitingTitan/temp.png')
        os.remove('data/waitingTitan/temp.png')

    @_waiting.command(pass_context = True)
    async def message(self, ctx):

        channel = ctx.message.channel
        now = datetime.utcnow()
        field_name_1 = "Date:"
        field_contents_1 = "{year}-{month:02d}-{day:02d}".format(year=now.year, month=now.month, day=now.day)
        field_name_2 = "Time:"
        field_contents_2 = "{hour:02d}:{minute:02d} UTC".format(hour=now.hour, minute=now.minute)
        embed = discord.Embed(colour=0xFF0000)  # Can use discord.Colour()
        embed.title = "There is Nothing New"
        embed.add_field(name=field_name_1, value=field_contents_1)  # Can add multiple fields.
        embed.add_field(name= field_name_2, value=field_contents_2)
        if channel.id not in self.json_data["Waiting"]:
            message = await self.bot.say(embed=embed)
            self.json_data["Waiting"][channel.id] = message.id
            dataIO.save_json(self.file_path, self.json_data)
        else:
            message = await self.bot.get_message(channel, self.json_data["Waiting"][channel.id])
            await self.bot.edit_message(message, embed = embed)



def check_folders(): # This is how you make your folder that will hold your data for your cog
    if not os.path.exists("data/waitingTitan"): # Checks if it exists first, if it does, then nothing executes
        print("Creating data/waitingTitan folder...")  # You can put what you want here. Prints in console for the owner
        os.makedirs("data/waitingTitan") # This makes the directory


def check_files(): # This is how you check if your file exists and let's you create it
    font = "data/waitingTitan/Codystar-Regular.ttf" # f is the path to the file
    data = "data/waitingTitan/Data.json"
    info = {"Waiting": {}}
    if not dataIO.is_valid_json(data):
        print("Creating default Data.json...") # Prints in console to let the user know we are making this file
        dataIO.save_json(data, info)

    if not os.path.isfile(font):
        print("retrieving Font File...")
        url = "https://fonts.google.com/download?family=Codystar"
        file_name = "data/waitingTitan/Codystar.zip"
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        zip_ref = zipfile.ZipFile("data/waitingTitan/Codystar.zip", 'r')
        zip_ref.extractall("data/waitingTitan")
        zip_ref.close()


def setup(bot):
    check_folders();
    check_files();
    if hasPil:
        bot.add_cog(waitingTitan(bot))
    else:
        print("Install Pillow using pip install Pillow")


def createImage():
    now = datetime.utcnow()
    font = ImageFont.truetype("data/waitingTitan/Codystar-Regular.ttf", 35)
    img = Image.new("RGBA", (500,150), (58,58,58))
    draw = ImageDraw.Draw(img)
    draw.text((25,20), "There Is Nothing New", (255,255,255), font=font)
    draw.text((110,60), "As of {year}-{month:02d}-{day:02d}".format(year=now.year, month=now.month, day=now.day), (255,255,255), font=font)
    draw.text((140,100), "At {hour:02d}:{minute:02d} UTC".format(hour=now.hour, minute=now.minute), (255,255,255), font=font)
    return img
