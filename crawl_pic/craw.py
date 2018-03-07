#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun


import re
import requests
from csv_rw import csv_to_list
from multiprocessing import Process
import os
from time import sleep


from requests.exceptions import RequestException
# total_list = csv_to_list('data/links.csv')

def get_pic(movie):
    url = 'http://www.imdb.com/title/tt'+movie
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            t1 = re.findall('class="poster"([\s\S]*?)jpg',html,re.S)
            if len(t1)>0:
                t2 = re.findall('https.*',t1[0])
                if len(t2)>0:
                    t3 = t2[0]+'jpg'
                    return t3
            else:
                return None
    except RequestException:
        print('Request Failed')

def go():
    total_list = csv_to_list('data/links.csv')
    with open('data/pics', 'a+') as f:
        for item in total_list:
            f.write(str(item[0])+','+item[1]+','+get_pic(item[1])+'\r\n')
            f.flush()
            print('finish: '+item[0])


def m_target(item):
    with open('data/pics1', 'a+') as f:
        f.write(str(item[0]) + ',' + item[1] + ',' + get_pic(item[1]) + '\r\n')
        f.flush()
        print('finish: '+item[0])

def go_m():
    total_list = csv_to_list('data/links.csv')
    for item in total_list:
        if not is_exist(item[0]):
            p=Process(target=m_target, args=(item,))
            p.start()
            sleep(0.15)



def get_finished_list():
    filename = 'data/pics1'
    finished_list = csv_to_list(filename,has_title=False)
    id = []
    for item in finished_list:
        id.append(item[0])
    return id

finished_id_list = get_finished_list()

def is_exist(movie):
    if movie in finished_id_list:
        return True
    return False



if __name__ == '__main__':
    file_links = 'data/links.csv'
    links_list = csv_to_list(file_links)
    for item in links_list:
        if not is_exist(item[0]):
            try:
                # print item[0] + '    '+ item[1]
                m_target(item)
            except TypeError:
                print 'ERROR:  '+item[0] + '    '+ item[1]