from bs4 import BeautifulSoup as bs
import requests
import lxml

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'


page = requests.get(url)

soup = bs(page.text, 'lxml')

data1 = soup.find('div',{'class':'status_wrap'})

data2 = data1.select('span')

find_dust = data2[5].text

print(find_dust)
