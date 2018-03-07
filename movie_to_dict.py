#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun


from csv_rw import csv_to_list


def movie_to_dict(movie_id):
    movie_id = str(movie_id)
    file_movies = 'ml-latest-small/movies.csv'
    file_links = 'ml-latest-small/links.csv'
    file_pics = 'ml-latest-small/pics.csv'
    movie = dict()
    movie['id'] = movie_id
    movies_list = csv_to_list(file_movies)
    links_list = csv_to_list(file_links)
    pics_list = csv_to_list(file_pics)
    for i in movies_list:
        if movie_id == i[0]:
            movie['title'] = i[1]
            #genres
            movie['genres'] = i[2].split('|')
            break
    for i in links_list:
        if movie_id == i[0]:
            movie['imdb_id'] = i[1]
    for i in pics_list:
        if movie_id == i[0]:
            movie['pic'] = i[2]
    return movie


if __name__ == '__main__':
    a = movie_to_dict(80)



