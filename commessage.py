# 부가 모듈 지정 (위치 지정 목적)
from telegram import *
from telegram.ext import *
from talk import *

# /start 함수
def start(update: Update, context:CallbackContext):
    update.message.reply_text("""안녕! 반가워.
나는 덕덕이가 만든 하나의 봇이야!
나는 가위바위보도 할줄 알고, 날씨도 알려줘!
많은 관심 부탁하구~ 앞으로 잘 이용하길 바래!
명령어 확인은 /help 를 확인해줘!
전달 기능은 아직 도입을 안했어! 그러니까 아무리 보내도 난 대답을 못해 ㅠ""")

# /help 함수
def help(update, context):
    update.message.reply_text('''가이드:
오늘의 날씨, 날씨, 오늘날씨, 오늘 날씨, 서울 날씨 ): 날씨 알려주는 커멘드
날짜, 오늘 날짜, 지금, 지금 날짜 ): 시간과 날짜를 알려주는 커멘드
미세먼지, 먼지 ): 미세먼지를 알려주는 커멘드
안녕: 인사해주는 봇(/start 동일 출력)
가위, 바위, 보 or 👊,✌️,🖐 ): 가위바위보 (이모티콘으로 보내면 이모티콘으로 출력 됌.)''')

# Message로 봇이 확인하여 작동하도록 해주는 함수
def tgtalk(update: Update, context:CallbackContext):
    text = str(update.message.text).lower()
    response = responsetext(text)
    update.message.reply_text(response)

