#!/usr/bin/env python3
# python-telegram-bot https://python-telegram-bot.org/
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from invitation import speaker
from send_mail import send_mail

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot for the TechWo Community Chapter Tuxtla!") # Welcome message

def invite(bot, update):
    name, org, email = update.message.text.split(",")
    speaker(name, org)
    send_mail(email)
    bot.send_document(chat_id=update.message.chat_id, document=open('./invitation/invitacion_ponencia.docx', 'rb'))

start_handler = CommandHandler('start', start)
invite_handler = MessageHandler(Filters.text, invite)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(invite_handler)

updater.start_polling()
