#! python3
# The birbs telegram bot
# Github: https://github.com/Zoidster/BirbBot

import telegram.ext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
import logging
import glob
import random
import ntpath
import os
import re
import shelve
from configobj import ConfigObj

from scraper import Scraper, ScraperConfig

shelve_filename_keyword = 'filename_hashes'
cache_subs = 'subs'


# Using ConfigObj
# Documentation: http://www.voidspace.org.uk/python/configobj.html
class BirbBot:
    def __init__(self, config_file):

        self.conf_file = config_file

        print('Reading config from file: {}'.format(self.conf_file))
        config = ConfigObj(self.conf_file)

        self.images_folder = config['images_folder']
        self.cache_file = config['birbs_cache_file']
        self.birbs_subreddit = config['birbs_subreddit']
        self.tinify_key = config["tinify_key"]

        reddit_conf = config['reddit']

        self.reddit_config = ScraperConfig(reddit_conf['reddit_client_id'],
                                           reddit_conf['reddit_client_secret'],
                                           reddit_conf['reddit_user_agent'],
                                           self.cache_file, shelve_filename_keyword)

        start_new_scraper(self.birbs_subreddit, self.get_image_folder(self.birbs_subreddit), self.reddit_config, self.tinify_key)

        if 'subreddits' in config:
            for subreddit in config['subreddits']:
                print('Adding scraper for subreddit {} to folder {}'.format(subreddit, config['subreddits'][subreddit]))
                start_new_scraper(subreddit, self.get_image_folder(config['subreddits'][subreddit]),
                                  self.reddit_config, self.tinify_key)

        print('Starting telegram bot')
        telegram_conf = config['telegram']
        self.start_bot(telegram_conf['telegram_bot_token'])
        print('Telegram bot started')

    def get_image_folder(self, path):
        return '{}/{}/'.format(self.images_folder, path)

    def start_bot(self, bot_token):
        updater = Updater(token=bot_token)

        dispatcher = updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        start_handler = CommandHandler('start', self.start_callback)
        dispatcher.add_handler(start_handler)

        birb_handler = CommandHandler('birb', self.birb_callback)
        dispatcher.add_handler(birb_handler)

        subscribe_handler = CommandHandler('subscribe', self.subscribe_callback, pass_args=True)
        dispatcher.add_handler(subscribe_handler)

        unsubscribe_handler = CommandHandler('unsubscribe', self.unsubscribe_callback, pass_args=True)
        dispatcher.add_handler(unsubscribe_handler)

        help_handler = CommandHandler('help', self.show_help_callback)
        dispatcher.add_handler(help_handler)

        add_handler = CommandHandler('add', self.add_callback, pass_args=True)
        dispatcher.add_handler(add_handler)

        unknown_handler = MessageHandler(Filters.command, self.unknown_callback)
        dispatcher.add_handler(unknown_handler)

        updater.start_polling()

        j = updater.job_queue
        j.run_repeating(self.callback_subs, interval=3600, first=3600/2)

    def callback_subs(self, bot, job):
        config = ConfigObj(self.conf_file)
        to_remove = []
        if cache_subs not in config:
            return
        for chat in config[cache_subs]:
            for folder in config[cache_subs][chat]:
                try:
                    print('Sending {} to chat {}'.format(folder, chat))
                    self.send_photo(bot, chat, folder)
                except Unauthorized as e:
                    to_remove.append(chat)
                   # print("removing chat from subs: {}\nError: {}".format(chat, e))

        # config[cache_subs] = [x for x in config[cache_subs] if x not in to_remove]
        # config.write()

    def birb_callback(self, bot, update):
        print('Sending birb to ' + update.message.from_user.name + ' - ' + update.message.text)
        self.send_birb(bot, update.message.chat_id)

    def start_callback(self, bot, update):
        other_image_folders = set([name for name in os.listdir(self.images_folder)
                                   if os.path.isdir(os.path.join(self.images_folder, name))])
        bot.send_message(chat_id=update.message.chat_id,
                         text='I am the birbs bot, I deliver the birbs.\n'
                              'Type /birb receive a brand new birb from our newest collection of premium birbs!.\n'
                              'Other content is available via the the following commands:\n' +
                              ', '.join(other_image_folders) + '\n' +
                              'Code located at https://github.com/Zoidster/BirbBot\n'
                              'Author: @LucaMN')

    def subscribe_callback(self, bot, update, args):
        if len(args) == 0:
            args = ['birbs']
        chat = str(update.message.chat_id)
        config = ConfigObj(self.conf_file)
        if cache_subs not in config:
            config[cache_subs] = {}
            config.write()
            config.reload()
        if chat not in config[cache_subs]:
            config[cache_subs][chat] = []
            config.write()
            config.reload()

        for folder in args:
            if folder not in config[cache_subs][chat]:
                chat_subs = config[cache_subs][chat]
                chat_subs.append(folder)
                config[cache_subs][chat] = chat_subs
                config.write()
                config.reload()
                print('Subscribtion of {} for chat {}'.format(folder, chat))
                bot.send_message(chat_id=update.message.chat_id,
                                 text='Subscription successful! Sending an image from {} every hour'.format(folder))
            else:
                bot.send_message(chat_id=update.message.chat_id,
                                 text='You are already subscribed to that!')

    def unsubscribe_callback(self, bot, update, args):
        chat = str(update.message.chat_id)
        config = ConfigObj(self.conf_file)
        if cache_subs not in config or chat not in config[cache_subs]:
            bot.send_message(chat_id=update.message.chat_id,
                             text='Unsubscription unsuccessful! You are not subscribed to anything')
            return

        for folder in args:
            if folder in config[cache_subs][chat]:
                chat_subs = config[cache_subs][chat]
                chat_subs.remove(folder)
                config[cache_subs][chat] = chat_subs
                config.write()
                config.reload()
                bot.send_message(chat_id=update.message.chat_id,
                                 text='Unsubscription successful! Not sending images from {} anymore'.format(folder))
            else:
                bot.send_message(chat_id=update.message.chat_id,
                                 text='Unsubscription unsuccessful! You are not subscribed to {}'.format(folder))

    def show_help_callback(self, bot, update):
        other_image_folders = set([name for name in os.listdir(self.images_folder)
                                   if os.path.isdir(os.path.join(self.images_folder, name))])
        bot.send_message(chat_id=update.message.chat_id,
                         text='Type /birb receive a brand new birb from our newest collection of premium birbs!\n' +
                              'Other content is available via the the following commands:\n' +
                              ', '.join(other_image_folders) + '\n' +
                              'Use the subscribe command with any amount of arguments to get hourly images\n'
                              'Code located at https://github.com/Zoidster/BirbBot\n'
                              'Author: @LucaMN')

    def add_callback(self, bot, update, args):
        config = ConfigObj(self.conf_file)

        # Extreme TODO move this to the config file

        if update.message.from_user.name != '@LucaMN':
            return

        # The subreddit is the name of the subreddit to pull the images from. It has to be alphanumeric
        subreddit = re.sub(r'\W+', '', args[0])

        if len(subreddit) == 0:
            bot.send_message(chat_id=update.message.chat_id,
                             text="This subreddit is invalid!")
            return

        # The handle is the folder and command the images will be accessible over. Also alphanumeric
        if len(args) > 1 and len(re.sub(r'\W+', '', args[1])) > 0:
            handle = re.sub(r'\W+', '', args[1])
        else:
            handle = subreddit

        s = Scraper(self.reddit_config,
                    self.get_image_folder(handle), subreddit, self.tinify_key)

        if s.sub_exists():
            if 'subreddits' not in config:
                config['subreddits'] = {subreddit: handle}
                config.write()
            else:
                config['subreddits'][subreddit] = handle
                config.write()

            bot.send_message(chat_id=update.message.chat_id,
                             text="Added the new subreddit to scrape, please wait a bit until the download is complete!")
            s.start()
            bot.send_message(chat_id=update.message.chat_id,
                             text="Scraping complete, {} images now available".format(handle))

        else:
            bot.send_message(chat_id=update.message.chat_id,
                             text="This subreddit does not exist!")
            del s

    def unknown_callback(self, bot, update):
        if self.images_folder != '':
            command = update.message.text[1:].split('@')[0]
            print('Sending {} to {}'.format(command, update.message.from_user.name))
            self.send_photo(bot, update.message.chat_id, command)

    def send_birb(self, bot, chat):
        self.send_photo(bot, chat, 'birb')

    def send_photo(self, bot, chat, command):
        if command == 'birb':
            command = 'birbs'

        image_folders = [name for name in os.listdir(self.images_folder)
                         if os.path.isdir(os.path.join(self.images_folder, name))]

        if command in image_folders:
            p = get_photo(self.cache_file, self.get_image_folder(command))
            if p is None:
                bot.send_message(chat_id=chat,
                                 text='There are no images in storage for the keyword {}'.format(command))
            else:
                photo, title = p
                bot.sendChatAction(chat_id=chat, action=telegram.ChatAction.UPLOAD_PHOTO)
                bot.send_photo(chat_id=chat, photo=open(photo, 'rb'),
                               caption=title)
        else:
            bot.send_message(chat_id=chat,
                             text="Sorry, I didn't understand the command {}.\n"
                                  "Type /help to see all commands".format(command))


def get_photo(cache_file, folder):
    settings = shelve.open(cache_file)

    photos = get_photos(folder)

    random.shuffle(photos)

    if len(photos) == 0:
        return None
    else:
        photo = photos[0]

    file_names = settings[shelve_filename_keyword]
    if ntpath.basename(photo) in file_names:
        title = file_names[ntpath.basename(photo)]
    else:
        title = os.path.splitext(ntpath.basename(photo))[0]

    settings.close()
    return photo, title


def get_photos(command):
    return glob.glob(command + '*')


def start_new_scraper(subreddit, folder, reddit_config, tinify_key):
    s = Scraper(reddit_config,
                folder, subreddit, tinify_key)
    s.start()
