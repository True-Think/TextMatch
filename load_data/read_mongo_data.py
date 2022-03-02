#!/usr/bin/env python
# -*- coding:utf-8 -*-
# FileName  :read_mongo_data.py
# Author    :evan.liu
# CreateTime:2022/3/2 17:15
# desc      :本代码主要功能如下
import json
import os
import pymysql
from pymongo import MongoClient
# from textmatch.config.constant import Constant as const


class OpMomngoDb(object):
    def __init__(self):
        client = MongoClient('mongodb://121.46.196.6:27017')
        CORPUS_TABLE_NAME = 'doc_base_info'
        self.doc_db_info = client.manager_doc_similar[CORPUS_TABLE_NAME]

    def get_doc_data(self, limit=None):
        if limit:
            corpus_cursor = self.doc_db_info.find({}, {"doc_id": 1, "doc_title": 1, "content": 1}).limit(limit)
        else:
            corpus_cursor = self.doc_db_info.find({}, {"doc_id": 1, "doc_title": 1, "content": 1})
        return corpus_cursor


class OpMysqlDb(object):
    def __init__(self):
        self.conn = pymysql.connect(
                host="43.132.254.152",
                port=3306,
                user="eric_select",
                password="Agj272Sgj2976_72hgSghiwy_ESgh92"
        )
        self.cursor = self.conn.cursor()

    def get_tags(self):

        sql = "SELECT id,title FROM jingliren_org.gp_keyword"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return {item[0]: item[1] for item in res}


def save_dict(file_name, dict_data):
    if dict_data:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=4)


def read_dict(file_name):
    result = None
    if file_name and os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            result = json.load(f)
    return result

