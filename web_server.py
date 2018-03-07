#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun


from flask import Flask
import use_recsys as rs
from movie_to_dict import movie_to_dict
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<int:user_id>')
def recommend(user_id):
    movies = rs.recommend_items_to_user(user_id,n=10)
    print movies
    result = []
    for movie in movies:
        d = movie_to_dict(movie)
        result.append(d)
    return json.dumps(result)


@app.route('/user/size')
def user_size():
    return str(rs.get_user_size())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
