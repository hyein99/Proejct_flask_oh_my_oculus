from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['POST'])
def listing():
    price = request.form['price']
    genre = request.form['genre']
    gamemode = request.form['gamemode']
    playmode = request.form['playmode']
    language = request.form['language']
    doc = {}
    if price == "0":
        doc['price'] = 0
    elif price == "2":
        doc['price'] = { '$lte': 20000 }
    elif price == "3":
        doc['price'] = { '$lte': 30000 }
    if genre:
        print(genre)
        doc['genre'] = { '$elemMatch': genre }

    apps = list(db.oculus.find(doc, {'_id': False}))
    return jsonify({'all_apps':apps})

## API 역할을 하는 부분
# @app.route('/memo', methods=['POST'])
# def saving():
#     url_receive = request.form['url_give']
#     comment_receive = request.form['comment_give']
#
#     doc = {
#         'url': url_receive,
#         'comment': comment_receive
#     }
#     db.articles.insert_one(doc)
#
#     return jsonify({'msg':'저장이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)