from telegram import *
from telegram.ext import *
from talk import responsetext as rt


def start(update: Update, context:CallbackContext):
    update.message.reply_text("hello")

def tgtalk(update: Update, context:CallbackContext):
    text = str(update.message.text).lower()
    response = rt(text)
    update.message.reply_text(response)

