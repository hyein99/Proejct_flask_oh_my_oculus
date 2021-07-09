import requests, json
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sparta

id = [2299465166734471, 2002317119880945, 1931356740318898, 1964070970347431, 2466379100068882]

# url = 'https://graph.oculus.com/graphql?forced_locale=ko_KR'

driver = webdriver.Chrome(executable_path='chromedriver')

for i in range(len(id)):
    url = 'https://www.oculus.com/experiences/quest/'+str(id[i])

    driver.get(url=url)
    driver.implicitly_wait(time_to_wait=5)

    # img, title, desc, price, game_mode, play_mode, genre, languages
    img = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[1]').get_attribute('style').split('"')[1]
    title = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]').text
    desc = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]').text
    price = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/button/div/div/span/span').text
    game_mode = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div[1]/div[2]/span').text.split(', ')
    play_mode = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div[2]/div[2]/a/span').text.split(', ')
    genre = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div[6]/div[2]/span').text.split(', ')
    languages = driver.find_element_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div[7]/div[2]/span').text.split(', ')

    db.oculus.insert_one({'title': title,
                          'img': img,
                          'desc': desc,
                          'price': price,
                          'game_mode': game_mode,
                          'play_mode': play_mode,
                          'genre': genre,
                          'languages': languages})