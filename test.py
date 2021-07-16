from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sparta

# game_mode, play_mode, category, genre, languages 종류
game_mode_set = set()
play_mode_set = set()
category_set = set()
genre_set = set()

apps = list(db.oculus.find({}, {'_id': False}))
for app in apps:
    game_mode_set |= set(app['game_mode'])
    play_mode_set |= set(app['play_mode'])
    category_set.add(app['category'])
    genre_set |= set(app['genre'])

print(game_mode_set)
print(play_mode_set)
print(category_set)
print(genre_set)
