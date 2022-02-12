import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

def weather():
    source = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&reg=100&auto_man=m&tm=2022.02.12.13:00&dtm=-12')
    soup = BeautifulSoup(source.content,"html.parser")

    table = soup.find('table',{'class':'table_develop3'})
    data = []

    print("#"*30)
    print("\nHello! Here's today's weather!\n")
    print("#"*30)
    
    for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))
        for td in tds:
            if td.find('a'):
                point = td.find('a').text
                temp = tds[5].text
                humidity = tds[9].text
                print("{0:<7} {1:<7} {2:<7}".format(point,temp,humidity))
                data.append([point,temp,humidity])
    
    print("#"*30)
    print("\nIt ends here. thanks!\n")
    print("#"*30)

    with open('weather.csv','w') as f:
        f.write('지역, 온도, 습도\n')
        for i in data:
            f.write('{0},{1},{2}\n'.format(i[0],i[1],i[2]))

 

 
