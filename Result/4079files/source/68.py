import logging
import socket
import traceback

from aiohttp import AsyncResolver, ClientSession, TCPConnector
import discord
from discord.ext import commands

from bot.config import BOT_CONFIG as CONFIG

log = logging.getLogger(__name__)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(*CONFIG.prefixes),
    activity=discord.Game(name=f"Commands: {CONFIG.prefixes[0]}help"),
    case_insensitive=True,
    fetch_offline_members=False,
    owner_id = CONFIG.owner_id
)
bot.log = log

# Global aiohttp session for all cogs
# - Uses asyncio for DNS resolution instead of threads, so we don't spam threads
# - Uses AF_INET as its socket family to prevent https related problems both locally and in prod.
bot.http_session = ClientSession(
    connector=TCPConnector(
        resolver=AsyncResolver(),
        family=socket.AF_INET,
    )
)

bot.db = CONFIG.db


@bot.event
async def on_ready():
    bot.owner = await bot.get_user_info(bot.owner_id)
    print(
        f'Succesfully logged in as {bot.user.name}#{bot.user.discriminator}...')


@bot.event
async def on_command_error(ctx: commands.Context, e: Exception):

    print(f"{type(e).__name__}: {e}")

    if isinstance(e, commands.CheckFailure):
        check = next(check for check in ctx.command.checks if not check(ctx))

        await ctx.send(embed=discord.Embed(
            title=f"Error with command: {ctx.command.name}",
            description=check.__doc__,
        ))
        return

    embed = discord.Embed(
        title=f"Error with command: {ctx.command.name}",
        description=f"```py\n{type(e).__name__}: {e}\n```"
    )
    await ctx.send(embed=embed)

    if isinstance(e, (commands.CommandError,
                      commands.MissingRequiredArgument,
                      commands.DisabledCommand,
                      commands.BadArgument,
                      commands.NoPrivateMessage,
                      commands.CheckFailure,
                      commands.CommandOnCooldown,
                      commands.MissingPermissions)):
        return

    embed.add_field(name="Channel:", value=f"<#{ctx.channel.id}>")
    embed.add_field(name="User:", value=f"<@{ctx.author.id}>")
    await bot.owner(embed=embed)

for cog in CONFIG.initial_cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f'Failed to load cog: {cog}')
        print(f'\t{type(e).__name__}: {e}')
        print(traceback.format_exc())


bot.run(CONFIG.token)
