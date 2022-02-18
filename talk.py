import datetime
import math
from bs4 import BeautifulSoup as bs
import requests



def responsetext(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hello~"

    if user_message in ('날짜', '오늘 날짜', '지금', '지금 날짜'):
        date = str(datetime.datetime.now())
        return date
    
    if user_message in ('미세먼지', '먼지'):
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        data1 = soup.find('div',{'class':'status_wrap'})
        data2 = data1.select('span')
        find_dust = data2[6].text
        return find_dust
    
    if user_message in ('오늘의 날씨', '날씨', '오늘날씨', '오늘 날씨', '서울 날씨'):
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        data1 = soup.find('div',{'class':'status_wrap'})
        data2 = data1.select('span')
        find_weather = data2[5].text
        return f"대한민국 서울특별시 중구의 날씨는 \"{find_weather}\"입니다."
    
