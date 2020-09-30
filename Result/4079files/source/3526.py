# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2017 - 2018 FrostLuma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord

from mousey import Mousey
from mousey.types import Buffer


class _LogChannel(Buffer):
    """Represents a single channel the LogEmitter emits logs to."""

    __slots__ = (
        '_buffer', '_can_emit', '_last_emit', '_task', 'ignored_exceptions', 'page_size', 'send_delay',
        'empty', 'events', 'destination',
    )

    def __init__(self, destination, empty, events, *, loop=None):
        super().__init__(loop=loop)

        # whether this channel logs no events, only specific messages
        self.empty = empty

        self.events = events
        self.destination = destination

    async def send(self, page):
        await self.destination.send(page)

    def is_visible_to(self, target=None):
        """Returns whether a user can view the current destination channel."""

        # if the target is not a discord.Member object they aren't in the guild - so they can't get mentioned
        if target is None or isinstance(target, discord.User):
            return False

        return self.destination.permissions_for(target).read_messages

    def does_log(self, event):
        """Returns whether this channel logs a specified event."""

        if self.empty:
            return False

        # if the list is empty everything is logged
        if not self.events:
            return True

        # else the list contains every event the logger logs
        return event in self.events


class LogEmitter:
    """
    Represents a ModLog logger. This is used to bulk up messages and prevent running into ratelimits.

    Parameters
    ----------
    mousey : Mousey
        The Bot the emitter logs for.
    """

    __slots__ = ('channels', 'mousey')

    def __init__(self, mousey):
        self.channels = {}
        self.mousey = mousey

    @classmethod
    def from_records(cls, records, *, mousey):
        """
        Creates a LogEmitter from a list of record objects.

        Parameters
        ----------
        records : List[asyncpg.Record]
            The records containing log channel information.
        mousey : Mousey
            The Bot the emitter logs for.
        """

        inst = cls(mousey)

        for record in records:
            inst.add_channel(record['channel_id'], record['events'])

        return inst

    def stop(self):
        for channel in self.channels.values():
            channel.stop()

    def add_channel(self, channel_id, events, *, empty=False):
        """
        Add a new channel this emitter logs to.

        Parameters
        ----------
        channel_id : int
            The ID of the channel to add.
        events : List[str]
            The events the channel logs. Empty if it logs all events.
        empty : bool
            Whether the channel logs no events, only specific messages sent to it. Defaults to False.
        """

        channel = _LogChannel(self.mousey.get_channel(channel_id), empty, events, loop=self.mousey.loop)
        self.channels[channel_id] = channel

        return channel

    def remove_channel(self, channel_id):
        """
        Remove a channel and stop it's emit task.

        Parameters
        ----------
        channel_id : int
            The ID of the channel to remove.
        """

        if channel_id not in self.channels:
            return len(self.channels)

        channel = self.channels.pop(channel_id)
        channel.task.cancel()

    def log(self, message, event, target):
        for channel in self.channels.values():
            if not channel.does_log(event):
                continue

            for idx, line in enumerate(message.split('\n')):
                # mention the target if it can't view the channel to allow moderators opening the profile
                if idx == 0 and target is not None and not channel.is_visible_to(target):
                    line = f'{line} {target.mention}'

                channel.queue(line)

    def log_to(self, message, destination, target):
        try:
            channel = self.channels[destination.id]
        except KeyError:
            self.channels[destination.id] = channel = self.add_channel(destination.id, [], empty=True)

        for idx, line in enumerate(message.split('\n')):
            # mention the target if it can't view the channel to allow moderators opening the profile
            if idx == 0 and target is not None and not channel.is_visible_to(target):
                line = f'{line} {target.mention}'

            channel.queue(line)
