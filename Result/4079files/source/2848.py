"""Definition of the bot's Admin module."""
import asyncio
import random
import discord
from contextlib import suppress
from util.perms import or_check_perms, echeck_perms, check_perms
from util.const import muted_perms
from discord.ext import commands
from .cog import Cog

class Admin(Cog):
    """Commands useful for admins and/or moderators.
    Can be extremely powerful, use with caution!
    """

    @commands.command(aliases=['clear', 'nuke', 'prune', 'clean']) # no_pm
    @commands.check(commands.guild_only())
    async def purge(self, ctx, *count):
        """Purge a channel of messages.
        Usage: purge"""
        if self.bot.selfbot:
            await ctx.send('**This command doesn\'t work in selfbot mode, due to a Discord restriction.**')
            return
        or_check_perms(ctx, ['manage_guild', 'manage_channels', 'manage_messages'])
        mode = 'count'
        detected = False
        if not count:
            limit = 1500
            detected = True
        elif len(count) == 1:
            if count[0] == 'infinite':
                limit = 1600
                detected = True
            else:
                try:
                    limit = abs(int(count[0])) + 1
                    if limit > 1600:
                        await ctx.send(ctx.mention + ' **You can only clean messages by user or 1-1600!**')
                        return
                    detected = True
                except ValueError:
                    pass
        if not detected:
            mode = 'target'
            targets = set()
            members = {}
            s = ctx.guild
            for i in getattr(s, 'members', []):
                members[i.mention] = i
                members[i.id] = i
                members[i.display_name] = i
                members[i.name] = i
            for i in count:
                try:
                    member = s.get_member(i)
                except AttributeError:
                    try:
                        member = await self.bot.get_user_info(i)
                    except discord.HTTPException:
                        member = None
                if member:
                    targets.add(member)
                else:
                    try:
                        member = await self.bot.get_user_info(i)
                    except discord.HTTPException:
                        member = None
                    if member:
                        targets.add(member)
            names = []
            _i = 0
            while _i < len(count):
                names.append(count[_i])
                with suppress(KeyError):
                    if ' '.join(names) in members:
                        targets.add(members[' '.join(names)])
                        names = []
                    elif _i + 1 == len(count):
                        targets.add(members[count[0]])
                        _i = -1
                        users = count[1:]
                        names = []
                _i += 1
            if not targets:
                await ctx.send('**No matching users, try again! Name, nickname, name#0000 (discriminator), or ID work. Spaces do, too!**')
                return
            purge_ids = [m.id for m in targets]
        try:
            if mode == 'count':
                deleted = await ctx.channel.purge(limit=limit)
            else:
                deleted = await ctx.channel.purge(limit=1500, check=lambda m: m.author.id in purge_ids)
        except discord.Forbidden:
            await ctx.send(ctx.mention + ' **I don\'t have enough permissions to do that here 😢**')
            return
        except discord.HTTPException as e:
            if '14 days old' in str(e):
                await ctx.send('I can only purge messages under 14 days old :sob:')
                return
            else:
                raise e
        dn = len(deleted)
        del_msg = await ctx.send('👏 I\'ve finished, deleting {0} message{1}!'.format((dn if dn else 'no'), ('' if dn == 1 else 's')))
        await asyncio.sleep(2.8)
        await del_msg.delete(reason='Deleting "finished purging" message')

    @commands.command(aliases=['amiadmin', 'isadmin', 'admin'])
    async def admintest(self, ctx):
        """Check to see if you're registered as a bot admin.
        Usage: admintest'"""
        tmp = check_perms(ctx, ('bot_admin',))
        if tmp:
            await ctx.send(ctx.mention + ' You are a bot admin! :smiley:')
        else:
            await ctx.send(ctx.mention + ' You are not a bot admin! :slight_frown:')

    @commands.command(aliases=['adminadd'])
    async def addadmin(self, ctx, *rrtarget: str):
        """Add a user to the bot admin list.
        Usage: addadmin [user]"""
        tmp = check_perms(ctx, ('bot_admin',))
        if not rrtarget:
            await ctx.send('**You need to specify a name, nickname, name#0000, mention, or ID!**')
            return
        rtarget = ' '.join(rrtarget)
        try:
            _target = ctx.guild.get_member_named(rtarget)
        except AttributeError:
            _target = None
        if _target:
            target = _target.id
        elif len(rtarget) == 18:
            target = rrtarget[0]
        elif ctx.message.mentions:
            target = ctx.message.mentions[0].id
        else:
            await ctx.send('**Invalid name! Name, nickname, name#0000, mention, or ID work.**')
            return
        if tmp:
            aentry = target
            if aentry not in self.bot.store['bot_admins']:
                self.bot.store['bot_admins'].append(aentry)
                await ctx.send('The user specified has successfully been added to the bot admin list!')
            else:
                await ctx.send('The user specified is already a bot admin!')
        else:
            await ctx.send(ctx.mention + ' You are not a bot admin, so you may not add others as admins!')

    @commands.command(aliases=['deladmin', 'admindel', 'adminrm'])
    async def rmadmin(self, ctx, *rrtarget: str):
        """Remove a user from the bot admin list.
        Usage: rmadmin [user]"""
        tmp = check_perms(ctx, ('bot_admin',))
        if not rrtarget:
            await ctx.send('**You need to specify a name, nickname, name#discriminator, or ID!**')
            return
        rtarget = ' '.join(rrtarget)
        try:
            _target = ctx.guild.get_member_named(rtarget)
        except AttributeError:
            _target = None
        if _target:
            target = _target.id
        elif len(rtarget) in range(15, 21):
            target = rrtarget[0]
        else:
            await ctx.send('**Invalid name! Name, nickname, name#discriminator, or ID work.**')
            return
        if tmp:
            aentry = target
            try:
                self.bot.store['bot_admins'].remove(aentry)
            except ValueError:
                await ctx.send('The user specified is not a bot admin!')
            else:
                await ctx.send('The user specified has successfully been demoted!')
        else:
            await ctx.send(ctx.mention + ' You are not a bot admin, so you may not demote other admins!')

    @commands.command(aliases=['admins'])
    async def adminlist(self, ctx):
        """List all bot admins defined.
        Usage: adminlist"""
        alist = ''
        for i in self.bot.store['bot_admins']:
            nid = ''
            try:
                _name = ctx.guild.get_member(i)
            except AttributeError:
                _name = None
            if not _name:
                try:
                    _name = await self.bot.get_user_info(i)
                except discord.NotFound:
                    _name = 'UNKNOWN'
                    nid = i
            if not nid:
                nid = _name.id
            alist += '**' + str(_name) + f'** (ID `{nid}`)\n'
        await ctx.send('The following people are bot admins:\n' + alist)

    @commands.command()
    @commands.check(commands.guild_only())
    async def getprop(self, ctx, pname: str):
        """Fetch a property from the datastore.
        Usage: getprop [property name]"""
        try:
            pout = self.bot.store.get_prop(ctx.message, pname)
        except Exception:
            await ctx.send('⚠ An error occured.')
            return
        await ctx.send(pout)

    @commands.command()
    @commands.check(commands.guild_only())
    async def setprop(self, ctx, pname: str, *, value: str):
        """Set the value of a property on guild level.
        Usage: setprop [property name] [value]"""
        echeck_perms(ctx, ('manage_guild',))
        self.bot.store.set_prop(ctx.message, 'by_guild', pname, value)
        await ctx.send(':white_check_mark:')

    @commands.command(aliases=['getprefix', 'setprefix'])
    async def prefix(self, ctx, *prefix: str):
        """Get or set the command prefix.
        Usage: prefix {new prefix}"""
        sk = ' guild'
        prop = ('by_guild', 'command_prefix')
        if self.bot.selfbot:
            sk = ''
            prop = ('global', 'selfbot_prefix')
        if prefix:
            or_check_perms(ctx, ['manage_guild', 'manage_channels', 'manage_messages'])
            jprefix = ' '.join(prefix)
            self.bot.store.set_prop(ctx.message, *prop, jprefix)
            await ctx.send(':white_check_mark:')
        else:
            oprefix = self.bot.store.get_cmdfix(ctx.message)
            await ctx.send('**Current%s command prefix is: **`%s`' % (sk, oprefix))

    async def progress(self, msg: discord.Message, begin_txt: str):
        """Play loading animation with dots and moon."""
        fmt = '{0}{1} {2}'
        anim = '🌑🌒🌓🌔🌕🌝🌖🌗🌘🌚'
        anim_len = len(anim) - 1
        anim_i = 0
        dot_i = 1
        while True:
            await msg.edit(content=fmt.format(begin_txt, ('.' * dot_i) + ' ' * (3 - dot_i), anim[anim_i]))
            dot_i += 1
            if dot_i > 3:
                dot_i = 1
            anim_i += 1
            if anim_i > anim_len:
                anim_i = 0
            await asyncio.sleep(1.1)

    @commands.command()
    @commands.check(commands.guild_only())
    async def mute(self, ctx, *, member: discord.Member):
        """Mute someone on voice and text chat.
        Usage: mute [person's name]"""
        or_check_perms(ctx, ['mute_members', 'manage_roles', 'manage_channels', 'manage_messages'])
        status = await ctx.send('Muting... 🌚')
        pg_task = self.loop.create_task(asyncio.wait_for(self.progress(status, 'Muting'), timeout=30, loop=self.loop))
        try:
            ch_perms = discord.PermissionOverwrite(**{p: False for p in muted_perms})
            for channel in ctx.guild.channels:
                await channel.set_permissions(member, ch_perms)
            await member.__redit(mute=True, deafen=None, reason='Mute command was used on user')
            pg_task.cancel()
            await status.delete(reason='Deleting progress/status message')
            await ctx.send('Successfully muted **%s**!' % str(member))
        except (discord.Forbidden, discord.HTTPException):
            pg_task.cancel()
            await status.delete(reason='Deleting progress/status message')
            await ctx.send('**I don\'t have enough permissions to do that!**')

    @commands.command()
    @commands.check(commands.guild_only())
    async def unmute(self, ctx, *, member: discord.Member):
        """Unmute someone on voice and text chat.
        Usage: unmute [person's name]"""
        or_check_perms(ctx, ('mute_members', 'manage_roles', 'manage_channels', 'manage_messages'))
        status = await ctx.send('Unmuting... 🌚')
        pg_task = self.loop.create_task(asyncio.wait_for(self.progress(status, 'Unmuting'), timeout=30, loop=self.loop))
        role_map = {r.name: r for r in member.roles}
        try:
            if 'Muted' in role_map:
                await member.remove_roles(role_map['Muted'], reason='Unmute command was used on user')
            ch_perms = discord.PermissionOverwrite(**{p: None for p in muted_perms})
            for channel in ctx.guild.channels:
                await channel.set_permissions(member, ch_perms)
            await member.__redit(mute=False, deafen=None, reason='Unmute command was used on user')
            pg_task.cancel()
            await status.delete(reason='Deleting progress/status message')
            await ctx.send('Successfully unmuted **%s**!' % str(member))
        except (discord.Forbidden, discord.HTTPException):
            pg_task.cancel()
            await status.delete(reason='Deleting progress/status message')
            await ctx.send('**I don\'t have enough permissions to do that!**')

    @commands.command()
    @commands.check(commands.guild_only())
    async def ban(self, ctx, *, member: discord.Member):
        """Ban someone from the guild.
        Usage: ban [member]"""
        echeck_perms(ctx, ('ban_members',))
        await ctx.send(':hammer: **Are you sure you want to ban ' + member.mention + '?**')
        if not (await self.bot.wait_for('message', timeout=6.0,
                                        check=lambda m: m.content.lower().startswith('y') and m.channel == ctx.channel and m.author == ctx.author)):
            await ctx.send('Not banning.')
            return
        await member.ban(reason='Ban was requested by command (from someone with the Ban Members permission)')
        await ctx.send(':hammer: Banned. It was just about time.')

def setup(bot):
    c = Admin(bot)
    bot.add_cog(c)
