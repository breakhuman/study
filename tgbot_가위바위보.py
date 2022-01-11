import telegram
import random
from telegram.ext import Updater, MessageHandler, Filters

# telegram token
bot = telegram.Bot(token = '5057996655:AAHKt-XRkTlB6LLsX6Fa2Wx-k18HrrgcCSc')

# 정보 받는거
for tginfo in bot.getUpdates():
    print(tginfo.message)
    
# 함수
sel = ['가위', '바위', '보']
result = {0: '승리', 1:'패배', 2:'비김'}