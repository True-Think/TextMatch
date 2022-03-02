#!/usr/bin/env python
# -*- coding:utf-8 -*-
# FileName  :test.py
# Author    :evan.liu
# CreateTime:2022/3/2 17:03
# desc      :本代码主要功能如下

##
'''
cd TextMatch
pip install -r requirements.txt
export PYTHONPATH=${PYTHONPATH}:../TextMatch
'''

import os
from textmatch.models.text_embedding.model_factory_sklearn import ModelFactory
from load_data.read_mongo_data import OpMysqlDb, save_dict, read_dict

if __name__ == '__main__':
    # doc
    file_name = "data/tags/all_tags.json"
    doc_dict = {
	
	'6659': '职场中的生存法则',
	'2988': '职场为人处世人际关系',
	'9617': '职场为人处事的技巧',
	'10024': '职场交往的原则',
	'12005': '职场交际技巧',
	'9163': '职场人品很重要',
	'9162': '职场人品的重要性',
	'9613': '职场人情世故',
	'9615': '职场人情冷暖',
	'9614': '职场人情往来',
	'3896': '职场人际',
	'9294': '职场人际交往',
	'2998': '职场人际交往原则与方法是什么',
	'2997': '职场人际交往原则与方法有哪些',
	'2999': '职场人际交往技巧',
	'3003': '职场人际交往的技巧有哪些',
	'5267': '职场人际关系',
	'3002': '职场人际关系与沟通技巧',
	'3000': '职场人际关系与沟通技巧总结',
	'3037': '职场人际关系处理技巧',
	'3033': '职场人际关系处理的四个建议',
	'3032': '职场人际关系的沟通技巧',
	'3034': '职场人际关系的重要性',
	'3094': '职场人际沟通交流技巧',
	'3102': '职场人际沟通技巧总结'
}
    #doc_dict = {}
    if not doc_dict:
        if not os.path.exists(file_name):
            my_db = OpMysqlDb()
            doc_dict = my_db.get_tags()
            save_dict(file_name, doc_dict)
        else:
            doc_dict = read_dict(file_name)
    print("tag len:", len(doc_dict))
    # doc_dict = {"0": "我去玉龙雪山并且喜欢玉龙雪山玉龙雪山", "1": "我在玉龙雪山并且喜欢玉龙雪山", "2": "我在九寨沟", "3": "你好"}
    # query
    query = "事业单位面试技巧"

    # 模型工厂，选择需要的模型加到列表中: 'bow', 'tfidf', 'ngram_tfidf', 'bert', 'albert', 'w2v'
    mf = ModelFactory(match_models=['bow', 'tfidf', 'ngram_tfidf'])
    # 模型处理初始化
    mf.init(words_dict=doc_dict, update=True)

    # query 与 doc的相似度
    search_res = mf.predict(query)
    print('search_res>>>>>', search_res)
    # search_res>>>>> {'bow': [('0', 0.2773500981126146), ('1', 0.5303300858899106), ('2', 0.8660254037844388), ('3', 0.0)], 'tfidf': [('0', 0.2201159065358879), ('1', 0.46476266418455736), ('2', 0.8749225357988296), ('3', 0.0)], 'ngram_tfidf': [('0', 0.035719486884261346), ('1', 0.09654705406841395), ('2', 0.9561288696241232), ('3', 0.0)]}

    # query的embedding
    # query_emb = mf.predict_emb(query)
    # print('query_emb>>>>>', query_emb)
    '''
    pre_emb>>>>> {'bow': array([1., 0., 0., 1., 1., 0., 1., 0.]), 'tfidf': array([0.61422608, 0.        , 0.        , 0.4842629 , 0.4842629 ,
       0.        , 0.39205255, 0.        ]), 'ngram_tfidf': array([0.        , 0.        , 0.37156534, 0.37156534, 0.        ,
       0.        , 0.        , 0.29294639, 0.        , 0.37156534,
       0.37156534, 0.        , 0.        , 0.37156534, 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.29294639, 0.37156534, 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        ])}
    '''