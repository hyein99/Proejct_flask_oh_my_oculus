from selenium import webdriver
from pymongo import MongoClient
import re

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.sparta

# chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

path = '/home/ubuntu/final/crawling/chromedriver'
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

# 각 application url 접속
file = open('urls.txt', 'r')
urls = file.readlines()
for i in range(135, len(urls)):
    url = urls[i].strip()
    print(i, url)

    driver.get(url=url)
    driver.implicitly_wait(time_to_wait=5)

    img, title, desc = '', '', ''
    price = 0
    doc = {}

    while True:
        img_path = driver.find_elements_by_xpath('//*[@id="mount"]/div/div[2]/div/div/div[1]')
        if img_path:
            img = img_path[0].get_attribute('style').split('"')[1]
            break
        driver.get(url=url)
        driver.implicitly_wait(time_to_wait=7)

    title_path = driver.find_element_by_xpath(
            '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]')
    if title_path:
        title = title_path.text
        desc = driver.find_element_by_xpath(
            '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]').text

        price_text = driver.find_element_by_xpath(
            '//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/button/div/div/span/span').text
        if price_text[0] == '₩':
            price = int(re.sub('₩|,', '', price_text))

        doc['title'] = title
        doc['img'] = img
        doc['desc'] = desc
        doc['price'] = price
        doc['url'] = url

        table = driver.find_elements_by_class_name('app-details-row')
        for row in table:
            if len(row.text.split('\n')) > 1:
                left = row.text.split('\n')[0]
                if left == 'Category':
                    right = row.text.split('\n')[1]
                else:
                    right = row.text.split('\n')[1].split(', ')
                doc[left] = right

    # print(doc)

    db.oculus2.insert_one(doc)
