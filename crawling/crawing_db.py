import requests, json
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
import re

# all application 정보 접속
url = 'https://www.oculus.com/experiences/quest/section/1888816384764129/'
data = {'access_token': 'OC|131781034909742|',
		'variables': {"sectionId":"1888816384764129",
					  "sortOrder":'null',
					  "sectionItemCount":'16',
					  "sectionCursor":"QVFIUm5Zenczem1tSjlKeWprV3pyV2dtdnlNUkFMR0VKT3g4NmxzbDllRktud25SWWx0RnFpZW5lelNlOEpKRUNxa1g6MjcwOTQwMjA=",
					  "hmdType":"MONTEREY"},
		'doc_id': 3730615617021634}
res = requests.post(url, data)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
app_script = soup.find("script", {"type": ["application/ld+json"]}).contents[0]
app_list = json.loads(app_script)['itemListElement']

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework

orders = list(db.order.find({}, {'_id': False}))
print(orders)

# driver = webdriver.Chrome(executable_path='chromedriver')
#
# # game_mode, play_mode, category, genre, languages 종류
# game_mode_set = set()
# play_mode_set = set()
# category_set = set()
# genre_set = set()
# languages_set = set()
#
# # 각 application url 접속
# for i in range(len(app_list)):
#     url = app_list[i]['url']
#     print(i, url)
#
#     driver.get(url=url)
#     driver.implicitly_wait(time_to_wait=5)
#
#     # img, title, desc, price, game_mode, play_mode, category, genre, languages
#     img, title, desc, category = '', '', '', ''
#     price = 0
#     game_mode, play_mode, genre, languages = [], [], [], []
#
#     while True:
#         img_path = driver.find_elements_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[1]')
#         if img_path:
#             img = img_path[0].get_attribute('style').split('"')[1]
#             break
#         driver.get(url=url)
#         driver.implicitly_wait(time_to_wait=7)
#
#     title_path = driver.find_element_by_xpath(
#             '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]')
#     if title_path:
#         title = title_path.text
#         desc = driver.find_element_by_xpath(
#             '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]').text
#
#         price_text = driver.find_element_by_xpath(
#             '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/button/div/div/span/span').text
#         if price_text[0] == '₩':
#             price = int(re.sub('₩|,', '', price_text))
#
#         game_mode_path = driver.find_elements_by_xpath(
#             "//*[contains(text(), '게임 모드')]/following-sibling::div/span")
#         if game_mode_path:
#             game_mode_list = game_mode_path[0].text.split(', ')
#             game_mode.extend(game_mode_list)
#             game_mode_set |= set(game_mode_list)
#
#         play_mode_path = driver.find_elements_by_xpath(
#             "//*[contains(text(), '지원되는 플레이 모드')]/following-sibling::div/a/span")
#         if play_mode_path:
#             play_mode_list = play_mode_path[0].text.split(', ')
#             play_mode.extend(play_mode_list)
#             play_mode_set |= set(play_mode_list)
#
#         category_path = driver.find_elements_by_xpath(
#             "//*[contains(text(), '카테고리')]/following-sibling::div/span")
#         if category_path:
#             category = category_path[0].text
#             category_set.add(category)
#
#         genre_path = driver.find_elements_by_xpath(
#             "//*[contains(text(), '장르')]/following-sibling::div/span")
#         if genre_path:
#             genre_list = genre_path[0].text.split(', ')
#             genre.extend(genre_list)
#             genre_set |= set(genre_list)
#
#         languages_path = driver.find_elements_by_xpath(
#             "//*[contains(text(), '언어')]/following-sibling::div/span")
#         if languages_path:
#             languages_list = languages_path[0].text.split(', ')
#             languages.extend(languages_list)
#             languages_set |= set(languages_list)
#
#     # db 삽입
#     doc = {
#         'title': title,
#         'img': img,
#         'desc': desc,
#         'price': price,
#         'game_mode': game_mode,
#         'play_mode': play_mode,
#         'category': category,
#         'genre': genre,
#         'languages': languages,
#         'url': url
#     }
#     db.oculus.insert_one(doc)
#     # print(title, img, desc, price, game_mode, play_mode, category, genre, languages, sep='\n')
#     # print('*'*50)
#
# print(game_mode_set)
# print(play_mode_set)
# print(category_set)
# print(genre_set)
# print(languages_set)