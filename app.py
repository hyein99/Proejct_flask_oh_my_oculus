from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/all', methods=['POST'])
def listing():
    price = request.form['price']
    genre = request.form['genre']
    gamemode = request.form['gamemode']
    playmode = request.form['playmode']
    language = request.form['language']
    doc = {}
    if price:
        doc['price'] = { '$lte': int(price)*10000 }
    if genre:
        doc['genre'] = {'$in': [genre]}
    if gamemode:
        doc['game_mode'] = {'$in': [gamemode]}
    if playmode:
        doc['play_mode'] = {'$in': [playmode]}
    if language:
        doc['languages'] = {'$in': [language]}

    apps = list(db.oculus.find(doc, {'_id': False}))
    return jsonify({'all_apps':apps})

@app.route('/app')
def apphome():
   return render_template('application.html')

@app.route('/app', methods=['GET'])
def application():
    title_receive = request.args.get('title_give')
    oapp = db.oculus.find_one({'title': title_receive},
                              {'_id': False})
    return jsonify({'oculus_app':oapp})

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