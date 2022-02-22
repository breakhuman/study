# 부가 모듈 지정
import datetime
import math
from bs4 import BeautifulSoup as bs
import requests
import random


# 대화 리스트
def responsetext(input_text):
    user_message = str(input_text).lower()
    
    # 영어 인사
    if user_message in ("hello", "hi", "sup"):
        return "Hello~"
    
    # 인사
    if user_message in ("안녕", "안녕하세요", "ㅎㅇ", '헬로', "헬로우", "안뇽", '안뇨옹'):
        return """안녕! 반가워.
        나는 덕덕이가 만든 하나의 봇이야!
        나는 가위바위보도 할줄 알고, 날씨도 알려줘!
        많은 관심 부탁하구~ 앞으로 잘 이용하길 바래!
        전달 기능은 아직 도입을 안했어! 그러니까 아무리 보내도 난 대답을 못해 ㅠ"""

    # 날짜
    if user_message in ('날짜', '오늘 날짜', '지금', '지금 날짜'):
        date = str(datetime.datetime.now())
        return date
    
    # 미세먼지
    if user_message in ('미세먼지', '먼지'):
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        data1 = soup.find('div',{'class':'status_wrap'})
        data2 = data1.select('span')
        find_dust = data2[6].text
        return f"대한민국 서울특별시 중구의 미세먼지는 \'{find_dust}\'입니다"
    
    # 날씨
    if user_message in ('오늘의 날씨', '날씨', '오늘날씨', '오늘 날씨', '서울 날씨'):
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        data1 = soup.find('div',{'class':'status_wrap'})
        data2 = data1.select('span')
        find_weather = data2[5].text
        return f"대한민국 서울특별시 중구의 날씨는 \'{find_weather}\'입니다."
    
    #가위바위보
    computer = random.choice(['가위','바위','보'])
    player = str(input_text).lower()

    if player in '가위':
        if computer == '가위':
            return f'컴퓨터:{computer} 비겼습니다.'
        if computer == '바위':
            return f'컴퓨터:{computer} 졌습니다.'
        if computer == '보':
            return f'컴퓨터:{computer} 이겼습니다.'
    if player in '바위':
        if computer == '가위':
            return f'컴퓨터:{computer} 이겼습니다.'
        if computer == '바위':
            return f'컴퓨터:{computer} 비겼습니다.'
        if computer == '보':
            return f'컴퓨터:{computer} 졌습니다.'
    if player in '보':
        if computer == '가위':
            return f'컴퓨터:{computer} 졌습니다.'
        if computer == '바위':
            return f'컴퓨터:{computer} 이겼습니다.'
        if computer == '보':
            return f'컴퓨터:{computer} 비겼습니다.'
    if player in ('👊','✌️','🖐'):
        return random.choice(['👊','✌️','🖐'])


