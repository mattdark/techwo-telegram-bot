#!/usr/bin/env python
# python-telegram-bot https://python-telegram-bot.org/
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import operator
from invitation import speaker

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot for the TechWo Community Chapter Tuxtla!") # Welcome message

# Function that validates operation introduced and print the result
def invite(bot, update):
    name, org = update.message.text.split(",")
    speaker(name, org)
    bot.send_document(chat_id=update.message.chat_id, document=open('./invitation/invitacion_ponencia.pdf', 'rb'))

start_handler = CommandHandler('start', start)
#help_handler = CommandHandler('help', help)
invite_handler = MessageHandler(Filters.text, invite)
#button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
#dispatcher.add_handler(button_handler)
#dispatcher.add_handler(help_handler)
dispatcher.add_handler(invite_handler)

updater.start_polling()
