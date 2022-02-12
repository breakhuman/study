import datetime
import math



def responsetext(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hello~"

    if user_message in ('날짜', '오늘 날짜', '지금', '지금 날짜'):
        date = str(datetime.datetime.now())
        return date
    
    if user_message in ('날씨', '오늘 날씨'):
        return 
    
