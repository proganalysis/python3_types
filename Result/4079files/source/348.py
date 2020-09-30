import discord
from discord.ext import commands
from scales import add_scales, has_scales, start_scales

description = '''Official Zealot Gaming Discord bot!'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["events", "games", "general", "moderator", "music", "recruitment", "roster", "scales"]

bot = commands.Bot(command_prefix='!', description='Official Zealot Gaming Discord Bot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Zealot Gaming'))


# Welcome Message
@bot.event
async def on_member_join(member):
    # Define Channels
    channel_general = bot.get_channel('108369515502411776')
    channel_info = bot.get_channel('301486963813384192')
    channel_announcements = bot.get_channel('141622089885941760')
    channel_events = bot.get_channel('296694692135829504')
    channel_clifford = bot.get_channel('302181408787529728')

    wmsg = "Everyone welcome {0.mention} to Zealot Gaming! Have a great time here! :wink: " \
           "http://puu.sh/nG6Qe.wav".format(member)

    wpm = "Welcome to the **Zealot Gaming Discord Community**! We are glad you are have joined us! First things " \
          "first, take a look at the {0.mention} channel; it has lots of information about our community! Also check " \
          "out the {1.mention} channel for upcoming events and game nights! Important news will be posted in " \
          "{2.mention}. Finally, we have a friendly bot, me, Clifford! You can talk to me using various commands that" \
          " start with `!`. For example, you should head over to {3.mention} and type `!register` to register as an " \
          "official member and become a Squire! If you have any questions, feel free to ask in the server; and again " \
          "welcome and thanks for joining!".format(channel_info, channel_events, channel_announcements,
                                                   channel_clifford)

    # Send Welcome Message to general channel
    await bot.send_message(channel_general, wmsg)

    # Send Private Welcome Message
    await bot.send_message(member, wpm)

    # Start the Scales
    start_scales(member)


# Check Messages and Award Scales
@bot.event
async def on_message(message):
    member = message.author
    legal_channels = ['general', 'zealot-lounge', 'league-of-legends', 'overwatch',
                      'heroes-of-the-storm', 'other-games', 'anime-and-manga', 'music-and-art']

    # If the user is participating in a normal channel
    if message.channel.name in legal_channels:
        # Longer Messages get more points. Not many.
        if len(message.content) > 35:
            scales = 2
        else:
            scales = 1

        # Add Grant Scales to User
        if has_scales(member):
            add_scales(member, scales)
        else:
            start_scales(member)
            add_scales(member, scales)

    # Process the rest of the Commands
    await bot.process_commands(message)


# Goodbye Message
# @bot.event
# async def on_member_remove(member):
#    channel = bot.get_channel('108369515502411776')
#    fmt = ":wave: Goodbye {0}, we're sad to see you go!".format(member.name)
#    await bot.send_message(channel, fmt)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run('token-here')
