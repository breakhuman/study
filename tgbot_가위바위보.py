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
def handler(update, context):
    user = update.message.text 

# 가위바위보 과정
def checkWin(user, com):
    if not user in sel:
        print('잘못입력하였습니다. 다시 입력하세요')
        return False

    print(f'사용자 ( {user} vs {com} ) 컴퓨터')
    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])
    return True
# 출력
