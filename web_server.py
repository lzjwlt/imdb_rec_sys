#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun


from flask import Flask
import use_recsys as rs
from movie_to_dict import movie_to_dict
from movie_to_dict import get_user_id_list
import json
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return '<strong>Usage:</strong><br/>' \
           'Recommend n movies to user<br/>'\
           '<strong>Example:</strong>  GET /user/user_id?num=5<br/>' \
           'Default num=10'


@app.route('/user/<int:user_id>', methods={"POST","GET"})
def recommend(user_id):
    if str(user_id) not in get_user_id_list():
        return 'user id : "%s" not exists!' % user_id
    num = request.args.get('num')
    if num is not None:
        try:
            num = int(num)
        except ValueError as e:
            num = 10
    else:
        num = 10
    movies = rs.recommend_items_to_user(user_id,n=num)
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
