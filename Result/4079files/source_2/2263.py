import discord
from discord.ext import commands
from helpers import db


# ********************************************** #
# GROUPED COMMANDS : EVENTS ******************** #
# ********************************************** #

class Events:
    def __init__(self, bot):
        self.bot = bot

    # COMMAND: !events
    @commands.group(pass_context=True)
    async def events(self, ctx):
        """Manage events and attendance!"""

        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid command passed. Must be *add*, *description*, *edit*, *register*, or *remove*.')

    # COMMAND: !events add
    @events.command(name='add', pass_context=True, aliases=['create'])
    @commands.has_role("Staff")
    async def events_add(self, ctx, date: str, time: str, *, title: str):
        """Add an event to the Events List!
           Date **must** be in YYYY/MM/DD format. Time **must** be in UTC."""

        # Set #events Channel
        event_channel = self.bot.get_channel('296694692135829504')

        # Make sure we have a date.
        if date is None:
            await self.bot.say('Error: You must enter a date in YYYY/MM/DD format.')
            return

        # Make sure we have a time.
        if time is None:
            await self.bot.say('Error: You must enter a time in HH:MM format in UTC timezone.')
            return

        # Make sure we have a title.
        if date is None:
            await self.bot.say('Error: You must enter a title for the event.')
            return

        # Add Event to Database
        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO events (`date`,`time`,`title`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (date, time, title))
                event_id = cursor.lastrowid

                msg_text = "**Title**: {0} \n**Event ID**: {1} \n**Date & Time**: {2} at {3} (UTC)"

                # Add Message to Events Channel and Save Message ID
                message = await self.bot.send_message(event_channel, msg_text.format(title, event_id, date, time))

                cursor.execute('UPDATE events SET `message_id` = %s WHERE `event_id` = %s', (message.id, event_id))
                db.commit()
                cursor.close()

        except Exception as e:
            await self.bot.say('{0.mention}, there was an error adding the event to the list. '
                               .format(ctx.message.author) + str(e))
            return

        # Success Message
        await self.bot.say('{0.mention}, your event was successfully added. The event ID is: {1}.'
                           .format(ctx.message.author, event_id))

    # COMMAND: !events description
    @events.command(name='description', pass_context=True, aliases=['desc', 'describe'])
    @commands.has_role("Staff")
    async def events_description(self, ctx, event_id: int, *, desc: str):
        """Adds a Description to an Event Given an Event ID."""

        # EVENT CHANNEL ID: 296694692135829504
        event_channel = self.bot.get_channel('296694692135829504')

        # Make sure we have a date.
        if event_id is None:
            await self.bot.say('Error: You must enter an event ID. Check the #events channel.')
            return

        # Make sure we have a date.
        if desc is None:
            await self.bot.say('Error: You must enter a description.')
            return

        try:
            with db.cursor() as cursor:
                sql = "UPDATE events SET `description` = %s WHERE `event_id` = %s"
                cursor.execute(sql, (desc, event_id))
                cursor.execute("SELECT `message_id`, `date`, `time`, `title` FROM events WHERE `event_id` = %s", (event_id,))
                msg_row = cursor.fetchone()
                message = await self.bot.get_message(event_channel, msg_row['message_id'])

                msg_text = "**Title**: {0} \n**Event ID**: {1} \n**Date & Time**: {2} at {3} (UTC) \n**Description**: {4}"

                # Update Message in Events Channel with Description
                await self.bot.edit_message(message, msg_text.format(msg_row['title'], event_id, msg_row['date'], msg_row['time'], desc))

                db.commit()
                cursor.close()
        except Exception as e:
            await self.bot.say('{0.mention}, there was an error adding a description to the event.'
                               .format(ctx.message.author) + str(e))
            return

        # Success Message
        await self.bot.say('{0.mention}, the event was successfully updated with a description.'
                           .format(ctx.message.author))

    # COMMAND: !events remove
    @events.command(name='remove', pass_context=True, aliases=['delete'])
    @commands.has_role("Staff")
    async def events_remove(self, ctx, event_id: int):
        """Adds a Description to an Event Given an Event ID."""

        # EVENT CHANNEL ID: 296694692135829504
        event_channel = self.bot.get_channel('296694692135829504')

        # Make sure we have a date.
        if event_id is None:
            await self.bot.say('Error: You must enter an event ID. Check the #events channel.')
            return

        # Get the Message
        try:
            with db.cursor() as cursor:
                sql = "SELECT `message_id` FROM events WHERE `event_id` = %s"
                cursor.execute(sql, (event_id,))
                msg_id = cursor.fetchone()
                message = await self.bot.get_message(event_channel, msg_id['message_id'])

                await self.bot.delete_message(message)

                cursor.execute("DELETE FROM events WHERE `event_id` = %s", (event_id,))
                db.commit()
                cursor.close()
        except Exception as e:
            await self.bot.say('{0.mention}, there was an error removing the event: '
                               .format(ctx.message.author) + str(e))
            return

        # Success Message
        await self.bot.say('{0.mention}, the event was successfully removed from the events list.'
                           .format(ctx.message.author))


def setup(bot):
    bot.add_cog(Events(bot))
