from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.Chrome('./chromedriver')

driver.get('https://comic.naver.com/webtoon/weekday')
driver.implicitly_wait(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
daily_webtoon = soup.find('div', {'class':'end_page'}).find('div', id='container').find('div', id='content').find('div', {'class':'list_area daily_all'})

col = daily_webtoon.find_all('div', {'class':'col'})
info = []
title_list = []
for c in col:
    li = c.find('div', {'class':'col_inner'}).find('ul').find_all('li')        
    for l in li:
        driver.find_element_by_class_name('title').click()
        title = l.find('a', {'class':'title'}).text.strip()
        if title not in title_list: # 타이틀 목록에 없는 타이틀을 만났을 때만!
            title_list.append(title)
            try:
                # '다음 화를 미리 만나보세요'가 있는 경우
                pass
            except:
                # '다음 화를 미리 만나보세요'가 없는 경우
                pass
    break

# def extract_webtoon_info():
#     col = daily_webtoon.find_all('div', {'class':'col'})
#     info = []
#     for c in col:
#         li = c.find('div', {'class':'col_inner'}).find('ul').find_all('li')    
#         for l in li:
#             each_info = {
#                 'title':l.find('a', {'class':'title'}).text.strip(),
#                 'link':l.find('a', {'class':'title'}, href=True)['href'],
#                 }   
#             info.append(each_info)
#     return info

# def find_series_url_and_move(webtoon_info):
#     # for webtoon in webtoon_info:
#     webtoon_url = requests.get('https://comic.naver.com/' + webtoon_info['link'])
#     print('https://comic.naver.com/' + webtoon_info['link'])
#     print(webtoon_url)
#     link_soup = BeautifulSoup(webtoon_url.text, 'html.parser')
#     try:
#         find_url = link_soup.find('div', {'class':'end_page'}).find('div', id='container').find('div', id='content')
#         # .find('table', {'class':'viewList'})
#         # .find('tbody', {'class':'band_banner_v2'}).find('td').find('a', href=True)['href']
#         # webtoon['series_url'] = find_url
#         # print(find_url.prettify())
#     except:
#         pass
#         # webtoon['series_url'] = None
#     # print(webtoon_info)

click_each_webtoon_name()