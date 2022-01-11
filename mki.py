from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
import os

my_token = '5057996655:AAHKt-XRkTlB6LLsX6Fa2Wx-k18HrrgcCSc'

print('start telegram chat bot')

dir_now = os.path.dirname(os.path.abspath(__file__))  # real path to dirname


# message reply function
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


# help reply function
def help_command(bot, update) :
    update.message.reply_text("무엇을 도와드릴까요?")


# photo reply function
def get_photo(bot, update) :
    print("get photo")
    print(update.message)
    file_path = os.path.join(dir_now, 'from_telegram.png')
    photo_id = update.message.photo[-1].file_id  # photo 번호가 높을수록 화질이 좋음
    photo_file = bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text('photo saved')


# file reply function
def get_file(bot, update) :
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_now, update.message.document.file_name)
    bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('file saved')


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()