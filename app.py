from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
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
        doc['Genres'] = {'$in': [genre]}
    if gamemode:
        doc['Game Modes'] = {'$in': [gamemode]}
    if playmode:
        doc['Supported Player Modes'] = {'$in': [playmode]}
    if language:
        doc['Languages'] = {'$in': [language]}

    apps = list(db.oculus2.find(doc, {'_id': False}).sort('_id', -1))
    return jsonify({'all_apps':apps})


@app.route('/app', methods=['GET'])
def application():
    title_receive = request.args.get('title_give')
    oapp = db.oculus2.find_one({'title': title_receive},
                              {'_id': False})
    return render_template('application.html', oapp=oapp)


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)