from bs4 import BeautifulSoup
import requests

url = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(url.text, 'html.parser')
daily_webtoon = soup.find('div', {'class':'end_page'}).find('div', id='container').find('div', id='content').find('div', {'class':'list_area daily_all'})

def extract_webtoon_title():
    col = daily_webtoon.find_all('div', {'class':'col'})
    title = []
    for c in col:
        li = c.find('div', {'class':'col_inner'}).find('ul').find_all('li')    
        for l in li:
            title.append(l.find('a', {'class':'title'}).text.strip())
    return title

def find_series_link_and_move():
    pass
