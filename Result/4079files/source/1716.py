import sys
import asyncio

from urllib.parse import urlparse

import aiohttp

from bs4 import BeautifulSoup as BS

import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
from telepot.aio.delegate import include_callback_query_chat_id
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

likes = set()
dislikes = set()


class LentaReader(telepot.aio.helper.ChatHandler):

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                   InlineKeyboardButton(text='👍', callback_data='like'),
                   InlineKeyboardButton(text='👎', callback_data='dislike'),
               ]])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._session = aiohttp.ClientSession()
        self._edit_msg_ident = None
        self._editor = None

    async def send_list(self):
        answer = "*Тебе нравится:*\n"
        for text in likes:
            answer += '"{0}..."\n'.format(text[:50])
        answer += "*Тебе не нравится:*\n"
        for text in dislikes:
            answer += '"{0}..."\n'.format(text[:50])
        await self.sender.sendMessage(answer, parse_mode='Markdown')
        return

    async def on_chat_message(self, msg):

        if "sticker" in msg:
            await self.sender.sendSticker(msg["sticker"]["file_id"])
            return

        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg["text"] == "/start":
            await self.sender.sendMessage("Привет! Пришли мне URL на новость на lenta.ru.")
            return
        if msg["text"] == "/list":
            await self.send_list()
            return

        parsed_url = urlparse(msg["text"])
        if not parsed_url.scheme:
            await self.sender.sendMessage("Что-то не так с твоим адресом, попробуй еще")
            return
        elif parsed_url.netloc != "lenta.ru":
            await self.sender.sendMessage("Не похоже, что это URL на lenta.ru")
            return

        async with self._session.get(parsed_url.geturl()) as resp:
            soup = BS(await resp.text(), "lxml")
            sent = await self.sender.sendMessage(
                soup.find("div", {"class": "b-text"}).get_text(),
                reply_markup=self.keyboard
            )
            self._editor = telepot.aio.helper.Editor(self.bot, sent)
            self._edit_msg_ident = telepot.message_identifier(sent)

    async def _cancel_last(self):
        if self._editor:
            await self._editor.editMessageReplyMarkup(reply_markup=None)
            self._editor = None
            self._edit_msg_ident = None

    async def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        await self._cancel_last()
        if query_data == "like":
            await self.bot.answerCallbackQuery(query_id, text='Ништяк! Записал.')
            likes.add(msg["message"]["text"])
            if msg["message"]["text"] in dislikes:
                dislikes.remove(msg["message"]["text"])
        elif query_data == "dislike":
            await self.bot.answerCallbackQuery(query_id, text='Совсем отстой, да? Записал.')
            dislikes.add(msg["message"]["text"])
            if msg["message"]["text"] in likes:
                likes.remove(msg["message"]["text"])


def main(token):
    bot = telepot.aio.DelegatorBot(token, [
        include_callback_query_chat_id(
            pave_event_space()
        )(per_chat_id(types=['private']), create_open, LentaReader, timeout=10),
    ])

    loop = asyncio.get_event_loop()
    loop.create_task(MessageLoop(bot).run_forever())
    print('Listening ...')

    loop.run_forever()


if __name__ == "__main__":
    main(sys.argv[1])
