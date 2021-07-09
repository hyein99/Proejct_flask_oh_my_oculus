import requests, json
from bs4 import BeautifulSoup

# url = 'https://www.oculus.com/experiences/quest/1587090851394426/'
url = 'https://graph.oculus.com/graphql?forced_locale=ko_KR'
data = {'access_token': 'OC|1317831034909742|',
		'variables': {"itemId":"1587090851394426",
                      "first":5,
                      "last":"null",
                      "after":"null",
                      "before":"null",
                      "forward":'true',
                      "ordering":"null",
                      "ratingScores":"null",
                      "hmdType":"MONTEREY"},
		'doc_id': 5373392672732392}
headers = {
	# 'accept': '*/*',
	# 'accept-encoding': 'gzip, deflate, br',
	# 'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
	# 'content-length': '304',
	# 'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'datr=uT3kYAwf_F8jyunRdbEJ59Mm; oa=MTYyNTU3MDc0NS7bF8Iv2yHrbPyYLhdxfIkWBhSYk8Q.; _fbp=fb.1.1625570747818.958200756; dpr=2.0000000298023224; wd=722x1350',
	'origin': 'https://www.oculus.com',
	'referer': 'https://www.oculus.com/',
	# 'sec-ch-ua-mobile': '?1',
	# 'sec-fetch-dest': 'empty',
	# 'sec-fetch-mode': 'cors',
	# 'sec-fetch-site': 'same-site',
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
}
res = requests.post(url, data=json.dumps(data), headers=headers)
# res = requests.post(url, data=json.dumps(data), headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
# app_script = soup.find("script", {"type": ["application/ld+json"]}).contents[0]