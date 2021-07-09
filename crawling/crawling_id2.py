import requests, json
from bs4 import BeautifulSoup

headers = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-length': '343',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'datr=uT3kYAwf_F8jyunRdbEJ59Mm; oa=MTYyNTU3MDc0NS7bF8Iv2yHrbPyYLhdxfIkWBhSYk8Q.; _fbp=fb.1.1625570747818.958200756; dpr=2.0000000298023224; wd=722x1350',
	'origin': 'https://www.oculus.com',
	'referer': 'https://www.oculus.com/',
	'sec-ch-ua-mobile': '?1',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
}
url = 'https://www.oculus.com/experiences/quest/section/1888816384764129/'
# url = 'https://graph.oculus.com/graphql?forced_locale=ko_KR'
data = {'access_token': 'OC|131781034909742|',
		'variables': {"sectionId":"1888816384764129",
					  "sortOrder":'null',
					  "sectionItemCount":'16',
					  "sectionCursor":"QVFIUm5Zenczem1tSjlKeWprV3pyV2dtdnlNUkFMR0VKT3g4NmxzbDllRktud25SWWx0RnFpZW5lelNlOEpKRUNxa1g6MjcwOTQwMjA=",
					  "hmdType":"MONTEREY"},
		'doc_id': 3730615617021634}
res = requests.post(url, data)
# res = requests.post(url, data=json.dumps(data), headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
# app_script = soup.find("script", {"type": ["application/ld+json"]}).contents[0]
# app_list = json.loads(app_script)['itemListElement']
#
# for app in app_list:
# 	headers = {
# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 	data = requests.get(app['url'], headers=headers)
#
# 	soup = BeautifulSoup(data.text, 'html.parser')
# 	trs = soup.select('#old_content > table > tbody > tr')