#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Zhijun

import csv

def csv_to_list(file_name, has_title=True):
    csv_reader = csv.reader(open(file_name))
    item_list = []
    for row in csv_reader:
        item_list.append(row)
    if has_title:
        item_list.pop(0)
    return item_list

