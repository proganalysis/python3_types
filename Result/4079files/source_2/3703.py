import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from re import sub
from discord import Embed, Channel
from discord.ext.commands import command
from src.cogs.rpg.duel import Duel
from src.cogs.rpg.progress_bar import ProgressBar
from src.util.helpers import calc_req_xp
from src.storage.db import database
from src.util.bunk_user import BunkUser
from src.util.bunk_exception import BunkException
from src.util.constants import USER_NAME_REGEX
from src.bunkbot import BunkBot


"""
RPG commands  
"""
class BunkRPG:
    def __init__(self, bot: BunkBot):
        self.bot = bot
        self.duels = []
        BunkBot.on_bot_initialized += self.wire_decay_check
        BunkUser.on_level_up += self.ding


    # wire up the scheduler to handle
    # XP decay every day
    async def wire_decay_check(self) -> None:
        try:
            scheduler = AsyncIOScheduler()
            scheduler.add_job(self.check_decayed_xp, trigger="cron", hour=4, misfire_grace_time=120)
            scheduler.start()

            if not scheduler.running:
                asyncio.get_event_loop().run_forever()
        except Exception as e:
            await self.bot.handle_error(e, "wire_decay_check")


    # every day, tell bunkbot to check over
    # the users and see when their XP was last updated
    # and calculate decay accordingly
    async def check_decayed_xp(self) -> None:
        try:
            return
            #decays = []
            #no_xp_date = []
            #today = datetime.today().date()

            #for user in self.bot.users:
            #    b_user: BunkUser = user

            #    if not b_user.last_xp_updated:
            #        no_xp_date.append("{0} has no xp to decay".format(b_user.name))
            #    else:
            #        last_update = datetime.strptime(b_user.last_xp_updated, "%m/%d/%Y").date()
            #        delta = (today - last_update).days
            #        if delta > 1:
            #            decays.append("{0} has not had an xp update in {1} days! ({2})".format(b_user.name, delta, b_user.last_xp_updated))

            #await self.bot.debug("\n".join(decays))
            #await self.bot.debug("\n".join(no_xp_date))
        except Exception as e:
            await self.bot.handle_error(e, "check_decayed_xp")


    # DING - user has leveled up
    # inform them and update their server permissions
    async def ding(self, member, value, channel: Channel = None) -> None:
        if member.name != "fugwenna":
            if channel is None:
                channel = self.bot.general

            # todo VIP level 10?
            await self.bot.say_to_channel(channel, ":bell: DING! {0.mention} has advanced to level {1}!".format(member, value))


    # get the top 10 leader board
    # sorting by level and xp
    @command(pass_context=True, cls=None, help="Get the current leader board", aliases=["leaders", "ranks", "levels", "leaderboard"])
    async def leader(self, ctx) -> None:
        try:
            await self.bot.send_typing(ctx.message.channel)

            players = sorted([u for u in self.bot.users if u.xp is not None and u.level is not None and u.xp >= 0],
                             key=lambda x: (x.level, x.xp), reverse=True)[:9]

            names = []
            levels = []
            xps = []

            if players is None:
                await self.bot.say("Uhh.. try again, @fugwenna sucks at programming")
                return

            for p in players:
                names.append(sub(USER_NAME_REGEX, "", p.name))
                levels.append(str(p.level))
                xps.append(str(p.xp))

            embed = Embed(title="Leader board - top 10 users", color=int("19CF3A", 16))
            embed.add_field(name="Name", value="\n".join(names), inline=True)
            embed.add_field(name="Level", value="\n".join(levels), inline=True)
            embed.add_field(name="Total XP", value="\n".join(xps), inline=True)

            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.handle_error(e, "leaders", ctx)


    # allow users to print out their current level
    # or the level of another user, which will display
    # in n of 20 blocks based on pct to next level
    @command(pass_context=True, help="Print your current level", aliases=["xp", "rank"])
    async def level(self, ctx) -> None:
        try:
            await self.bot.send_typing(ctx.message.channel)

            user: BunkUser = self.bot.get_user_by_id(ctx.message.author.id)
            color = ctx.message.author.color

            params = self.bot.get_cmd_params(ctx)

            # user is getting the level of
            # another bunk user
            if len(params) > 0:
                param_user: BunkUser = self.bot.get_user(" ".join(params[0:]))
                user = param_user
                color = param_user.member.color

            progress_bar: ProgressBar = ProgressBar(user)
            embed = Embed(title="{0}: Level {1}".format(user.name, user.level), description=progress_bar.draw(), color=color)

            if len(params) > 0:
                embed.set_footer(text="{0} is currently {1}% to level {2}".format(user.name, progress_bar.pct, user.next_level))
            else:
                embed.set_footer(text="You are currently {0}% to level {1}".format(progress_bar.pct, user.next_level))

            await self.bot.say(embed=embed)

        except BunkException as be:
            await self.bot.say(be.message)
        except Exception as e:
            await self.bot.handle_error(e, "level", ctx)


    # challenge another user to a duel
    # if they are currently, dueling throw an error
    # a user cannot challenge themselves to a duel
    @command(pass_context=True, help="Challenge another user to a duel", aliases=["challenge2"])
    async def duel(self, ctx) -> None:
        try:
            challenger: BunkUser = self.bot.get_user_by_id(ctx.message.author.id)
            param = self.bot.get_cmd_params(ctx)

            if len(param) == 0:
                await self.bot.say("You must supply a challenger!")
                return

            opponent: BunkUser = self.bot.get_user(" ".join(param[0:]))
            challenger.duel = Duel(challenger, opponent)
            self.duels.append(challenger.duel)

            msg = """:triangular_flag_on_post: {0.mention} is challenging {1.mention} to a duel! 
            Type !accept to duel, or !reject to run away like a little biiiiiiiiiiiiitch""".format(challenger, opponent)

            await self.bot.say(msg)

        except BunkException as be:
            await self.bot.say(be.message)
        except Exception as e:
            await self.bot.handle_error(e, "duel", ctx)


    # accept a duel from another BunkUser
    # and lock the duel for both users
    @command(pass_context=True, help="Accept a duel")
    async def accept(self, ctx) -> None:
        try:
            bunk_user: BunkUser = self.bot.get_user_by_id(ctx.message.author.id)
            duels = [d for d in self.duels if d.opponent.name == bunk_user.name]

            if len(duels) == 0:
                await self.bot.say("You have no duels to accept")
                return

            duel: Duel = duels[0]
            await duel.execute()
            self.duels.remove(duel)

            embed = Embed(title=":crossed_swords: {0} vs {1}".format(duel.challenger.name, duel.opponent.name),
                          color=int("FF0000", 16))
            embed.add_field(name="Name", value="\n".join([duel.challenger.name, duel.opponent.name]), inline=True)
            embed.add_field(name="Damage",
                            value="\n".join([str(duel.challenger.duel_roll), str(duel.opponent.duel_roll)]),
                            inline=True)

            await self.bot.say(embed=embed)

            if duel.tie:
                await self.bot.say("{0}.mention {1}.mention - :necktie: It's a tie! :necktie:"
                                   .format(duel.challenger.mention, duel.opponent.mention))
                return

            xp_lost = 5.0
            if duel.loser.xp > 5.0:
                await self.bot.say("{0.mention} wins 5 xp from {1}!".format(duel.winner, duel.loser.name))
            elif 5.0 > duel.loser.xp > 0.0:
                xp_lost = duel.loser.xp
                await self.bot.say("{0.mention} wins {1}'s remaining xp!".format(duel.winner, duel.loser.name))
            elif duel.loser.xp == 0:
                await self.bot.say("{0.mention} wins, but {1} has no xp to give!".format(duel.winner, duel.loser.name))

            if duel.loser.xp > 0:
                database.update_user_xp(duel.loser.member.id, -xp_lost)

            loser_level_xp = calc_req_xp(duel.loser.level)

            if duel.loser.level > 1 and duel.loser.xp - xp_lost < loser_level_xp:
                duel.loser.from_database(database.update_user_level(duel.loser.member.id, -1))
                await self.bot.say("{0.mention} has lost a level!".format(duel.loser))

            if xp_lost > 0:
                await duel.winner.update_xp(xp_lost, ctx.message.channel, True)

        except BunkException as be:
            await self.bot.say(be.message)
        except Exception as e:
            await self.bot.handle_error(e, "accept", ctx)


    # reject a duel from another BunkUser
    # and remove the lock for both users
    @command(pass_context=True, cls=None, help="Reject a duel")
    async def reject(self, ctx) -> None:
        try:
            found = False
            user: BunkUser = self.bot.get_user_by_id(ctx.message.author.id)

            for d in self.duels:
                if d.opponent.name == user.name:
                    found = True
                    d.challenger.duel = None
                    d.opponent.duel = None
                    self.duels.remove(d)
                    await self.bot.say(":exclamation: {0.mention} has rejected a duel with {1.mention}".format(d.opponent, d.challenger))

            if not found:
                await self.bot.say("You have no duels to reject")

        except BunkException as be:
            await self.bot.say(be.message)
        except Exception as e:
            await self.bot.handle_error(e, "cancel", ctx)


    # cancel a duel from another BunkUser
    # and remove the lock for both users
    @command(pass_context=True, cls=None, help="Cancel a duel")
    async def cancel(self, ctx) -> None:
        try:
            found = False
            user: BunkUser = self.bot.get_user_by_id(ctx.message.author.id)

            for d in self.duels:
                if d.challenger.name == user.name:
                    found = True
                    d.challenger.duel = None
                    d.opponent.duel = None
                    self.duels.remove(d)
                    await self.bot.say("{0.mention} has cancelled their duel with {1.mention}".format(d.challenger, d.opponent))

            if not found:
                await self.bot.say("You have no duels to cancel")

        except BunkException as be:
            await self.bot.say(be.message)
        except Exception as e:
            await self.bot.handle_error(e, "cancel", ctx)


def setup(bot: BunkBot) -> None:
    bot.add_cog(BunkRPG(bot))