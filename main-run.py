# Module list
import logging
from telegram import *
from telegram.ext import *
from keys import token
from commessage import *

# Error 표출
def error(update, context):
    print(f"update {update} caused error {context.error}")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Main def 함수
def main() -> None:
    up = Updater(token, use_context=True)
    dp = up.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, tgtalk))
    dp.add_error_handler(error)
    up.start_polling()
    up.idle()

# 모듈로 실행하는 것을 막는 일종의 장치
if __name__=="__main__":
    main()