import requests, json
from bs4 import BeautifulSoup

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

with open('urls.txt', 'w') as f:
    for app in app_list:
        f.write('%s\n' % app['url'])
