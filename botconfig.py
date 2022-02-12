from telegram import *
from telegram.ext import *
from keys import token
from commessage import *

def main() -> None:
    up = Updater(token, use_context=True)
    dp = up.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, tgtalk))

    up.start_polling()
    up.idle()

main()