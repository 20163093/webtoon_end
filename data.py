from bs4 import BeautifulSoup
import requests

url = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(url.text, 'html.parser')
daily_webtoon = soup.find('div', {'class':'end_page'}).find('div', id='container').find('div', id='content').find('div', {'class':'list_area daily_all'})

def extract_webtoon_info():
    col = daily_webtoon.find_all('div', {'class':'col'})
    info = []
    for c in col:
        li = c.find('div', {'class':'col_inner'}).find('ul').find_all('li')    
        for l in li:
            each_info = {
                'title':l.find('a', {'class':'title'}).text.strip(),
                'link':l.find('a', {'class':'title'}, href=True)['href'],
                }   
            info.append(each_info)
    return info

def find_series_link_and_move(webtoon_info):
    for webtoon in webtoon_info:
        # print(webtoon['link'])
        webtoon_url = requests.get('https://comic.naver.com/' + webtoon['link'])
        link_soup = BeautifulSoup(webtoon_url.text, 'html.parser')
        print(webtoon_url.status_code)

webtoon_info = extract_webtoon_info()
find_series_link_and_move(webtoon_info)