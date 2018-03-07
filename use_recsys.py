#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun


from recsys.algorithm.factorize import SVD


svd = SVD()
svd.load_data(filename='ml-latest-small/ratings1.csv',
              sep=',',
              # format={'userId':0,'movieId':1,'rating':2,'ids':int})
              format={'col': 0, 'row': 1, 'value': 2, 'ids': int})

k = 100
svd.compute(k=k,
            min_values=10,
            pre_normalize=None,
            mean_center=True,
            post_normalize=True,
            savefile='/tmp/movielens')


def get_items_similarity(item_id1, item_id2):
    return svd.similarity(item_id1, item_id2)


def get_similar_items(item_id,n=10):
    return svd.similar(item_id,n)


def predict_item_rating_from_user(item_id, user_id, min_rating=1, max_rating=5):
    return svd.predict(item_id,user_id,min_rating,max_rating)


def get_user_size():
    size = svd.get_matrix().get_row_len()
    return size


def recommend_items_to_user(user_id, n=10, need_ratings=False):
    result = svd.recommend(user_id,n,is_row=False)
    if need_ratings:
        return result
    r = []
    for i in result:
        r.append(i[0])
    return r


def recommend_users_to_item(item_id, n=10, need_ratings=False):
    result = svd.recommend(item_id,n)
    if need_ratings:
        return result
    r = []
    for i in result:
        r.append(i[0])
    return r


