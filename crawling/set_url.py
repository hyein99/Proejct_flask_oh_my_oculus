import requests, json
from bs4 import BeautifulSoup
from pymongo import MongoClient

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
db = client.sparta

apps = list(db.oculus2.find({}, {'_id': False}))
for i in range(len(apps)):
    title = apps[i]['title']
    url = app_list[i]['url']
    db.oculus2.update_one({'title': title}, {'$set': {'url': url}})