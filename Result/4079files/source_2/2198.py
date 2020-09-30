import discord
from discord.ext import commands
import random


class General:
    def __init__(self, bot):
        self.bot = bot

    # ********************************************** #
    # UN-GROUPED BOT COMMANDS ********************** #
    # ********************************************** #

    # Load Extension
    @commands.command(pass_context=True)
    @commands.has_role("King")
    async def load(self, ctx, extension_name: str):
        """Loads an extension."""

        try:
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as ex:
            await self.bot.say("```py\n{}: {}\n```".format(type(ex).__name__, str(ex)))
            return
        await self.bot.say("{} loaded.".format(extension_name))

    # Unload Extension
    @commands.command(pass_context=True)
    @commands.has_role("King")
    async def unload(self, ctx, extension_name: str):
        """Unloads an extension."""

        self.bot.unload_extension(extension_name)
        await self.bot.say("{} unloaded.".format(extension_name))

    # COMMAND: !hello
    @commands.command(pass_context=True)
    async def hello(self, ctx):
        """Say hello to Clifford, and he will say hello to you."""
        # we do not want the bot to reply to itself
        if ctx.message.author == self.bot.user:
            return
        else:
            msg = 'Hello {0.message.author.mention}'.format(ctx)
            await self.bot.send_message(ctx.message.channel, msg)

    # COMMAND: !carlito
    @commands.command()
    async def carlito(self):
        """The legendary message of Carlito, maz00's personal cabana boy."""
        await self.bot.say(
            "wew men :ok_hand::skin-tone-1: that's some good shit:100: some good shit :100: that's some good shit"
            " right there :100: :ok_hand::skin-tone-1: right there :ok_hand::skin-tone-1: :100: sign me the FUCK "
            "up:100: :100: :ok_hand::skin-tone-1: :eggplant:")

    # COMMAND: !eightball
    @commands.command(pass_context=True)
    async def eightball(self, ctx, question: str):
        """Rolls a magic 8-ball to answer any question you have."""

        if not question:
            await self.bot.say('{0.message.author.mention}, you did not ask a question.'.format(ctx))
            return

        # Answers List (Classic 8-Ball, 20 Answers)
        answers = ['It is certain.',
                   'It is decidedly so',
                   'Without a doubt.',
                   'Yes, definitely.',
                   'You may rely on it.',
                   'As I see it, yes.',
                   'Most likely.',
                   'Outlook good.',
                   'Yes.',
                   'Signs point to yes.',
                   'Reply hazy; try again.',
                   'Ask again later.',
                   'Better not tell you now.',
                   'Cannot predict now.',
                   'Concentrate, then ask again.',
                   'Do not count on it.',
                   'My reply is no.',
                   'My sources say no.',
                   'Outlook not so good.',
                   'Very doubtful.']

        # Send the Answer
        await self.bot.say('{0.message.author.mention}, '.format(ctx) + random.choice(answers))

    # COMMAND: !roll
    @commands.command()
    async def roll(self, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    # COMMAND: !join
    @commands.command(pass_context=True)
    async def join(self, ctx, *, role: str):
        """Allows a user to join a public group."""

        role_name = role.lower()

        # List of Allowed Public Roles
        allowed_roles = ["eu",
                         "europe",
                         "na",
                         "north america",
                         "oce",
                         "oceania",
                         "lol",
                         "league of legends",
                         "coop",
                         "co-op",
                         "destiny",
                         "d2",
                         "destiny 2",
                         "ow",
                         "overwatch",
                         "anime hour",
                         "anime"]

        roles_dictionary = {"eu": "Europe",
                            "europe": "Europe",
                            "na": "North America",
                            "north america": "North America",
                            "oce": "Oceania",
                            "oceania": "Oceania",
                            "lol": "League of Legends",
                            "league of legends": "League of Legends",
                            "coop": "Co-op",
                            "co-op": "Co-op",
                            "destiny": "Destiny 2",
                            "d2": "Destiny 2",
                            "destiny 2": "Destiny 2",
                            "ow": "Overwatch",
                            "overwatch": "Overwatch",
                            "anime hour": "Anime Hour",
                            "anime": "Anime Hour"}

        if role_name not in allowed_roles:
            await self.bot.say('{0.mention}, you may only join allowed public groups. Check #info for a list of groups.'
                               .format(ctx.message.author))
            return

        # Define role, then add role to member.
        try:
            role = discord.utils.get(ctx.message.server.roles, name=roles_dictionary[role_name])
            await self.bot.add_roles(ctx.message.author, role)
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, "{0.mention}, there was an error joining the group: "
                                                             "".format(ctx.message.author) + str(e))
            return

        # Success Message
        await self.bot.say('{0.mention}, you have successfully been added to the group **{1}**'
                           '.'.format(ctx.message.author, roles_dictionary[role_name]))

    # COMMAND: !leave
    @commands.command(pass_context=True)
    async def leave(self, ctx, *, role: str):
        """Allows a user to leave a public group."""

        role_name = role.lower()

        # List of Allowed Public Roles
        allowed_roles = ["eu",
                         "europe",
                         "na",
                         "north america",
                         "oce",
                         "oceania",
                         "lol",
                         "league of legends",
                         "coop",
                         "co-op",
                         "destiny",
                         "d2",
                         "destiny 2",
                         "ow",
                         "overwatch",
                         "anime hour",
                         "anime"]

        roles_dictionary = {"eu": "Europe",
                            "europe": "Europe",
                            "na": "North America",
                            "north america": "North America",
                            "oce": "Oceania",
                            "oceania": "Oceania",
                            "lol": "League of Legends",
                            "league of legends": "League of Legends",
                            "coop": "Co-op",
                            "co-op": "Co-op",
                            "destiny": "Destiny 2",
                            "d2": "Destiny 2",
                            "destiny 2": "Destiny 2",
                            "ow": "Overwatch",
                            "overwatch": "Overwatch",
                            "anime hour": "Anime Hour",
                            "anime": "Anime Hour"}

        if role_name not in allowed_roles:
            await self.bot.say(
                '{0.mention}, you may only join allowed public groups. Check #info for a list of groups.'
                .format(ctx.message.author))
            return

        # Define role, then add role to member.
        try:
            role = discord.utils.get(ctx.message.server.roles, name=roles_dictionary[role_name])
            await self.bot.remove_roles(ctx.message.author, role)
        except Exception as e:
            await self.bot.send_message(ctx.message.channel,
                                        "{0.mention}, there was an error leaving the group: "
                                        "".format(ctx.message.author) + str(e))
            return

        # Success Message
        await self.bot.say('{0.mention}, you have successfully left the group **{1}**'
                           '.'.format(ctx.message.author, roles_dictionary[role_name]))

    # COMMAND: !register
    @commands.command(pass_context=True)
    async def register(self, ctx):
        """Allows a user to register officially and become a Squire."""

        # List of Allowed Public Roles
        member = ctx.message.author
        role_names = [r.name for r in member.roles]
        registered_roles = ['Squire', 'Knight', 'Zealot']
        squire = discord.utils.get(ctx.message.server.roles, name='Squire')

        if not set(role_names) & set(registered_roles):

            # Define role, then add role to member.
            try:
                await self.bot.add_roles(member, squire)
            except Exception as e:
                await self.bot.say('There was an error registering you'.format(ctx.message.author) + str(e))
                return

            # Success Message
            await self.bot.say('{0.mention}, you have successfully registered and been promoted to **Squire**'
                               .format(member))
        else:
            await self.bot.say('{0.mention}, you are already registered!'.format(member))

    # COMMAND: !serverinfo
    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Displays Information about the Server."""

        # Regions Dictionary
        region_dictionary = {"us-west": "US West",
                             "us-east": "US East",
                             "us-central": "US Central",
                             "eu-west": "EU West",
                             "eu-central": "EU Central",
                             "singapore": "Singapore",
                             "london": "London",
                             "syndey": "Sydney",
                             "amsterdam": "Amsterdam",
                             "frankfurt": "Frankfurt",
                             "brazil": "Brazil"}

        # Online Status
        online_statuses = ["online", "idle", "dnd", "do_not_disturb"]

        # GET EMBED INFO
        server = ctx.message.server
        server_name = server.name
        server_region = region_dictionary[str(server.region)]
        server_date = server.created_at.strftime('%B %d, %Y')
        server_icon = server.icon_url
        server_total_members = server.member_count
        server_id = server.id
        server_owner = server.owner
        server_online_members = sum(1 for member in server.members if str(member.status) in online_statuses)
        server_text_channels = sum(1 for channel in server.channels if str(channel.type) == "text")
        server_voice_channels = sum(1 for channel in server.channels if str(channel.type) == "voice")
        server_roles = sorted(server.roles, key=lambda role: role.position, reverse=True)
        server_roles_list = ", ".join(role.name for role in server_roles if role.hoist is True)

        # Create Embed Table
        embed = discord.Embed(title=server_name, colour=1203153,
                              description="Created on " + server_date)
        embed.set_thumbnail(url=server_icon)
        embed.set_footer(text="Server ID: " + server_id)
        embed.add_field(name="Owner", value="{0.mention}".format(server_owner), inline=True)
        embed.add_field(name="Location", value=server_region, inline=True)
        embed.add_field(name="Online Members", value=server_online_members, inline=True)
        embed.add_field(name="Total Members", value=server_total_members, inline=True)
        embed.add_field(name="Text Channels", value=server_text_channels, inline=True)
        embed.add_field(name="Voice Channels", value=server_voice_channels, inline=True)
        embed.add_field(name="Roles", value=server_roles_list, inline=False)

        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
