import gensim
from spider import *
from text_transform import text_transform
from LDA import *
from write2mysql import ConnectMysql
from seed_keywords import seed_keywords


model = gensim.models.KeyedVectors.load_word2vec_format('model/sgns.wiki.word')

# print(model.most_similar(['男人']))     # 返回与指定词语最相近的几个词以及与对应的相似度
# print(model.similarity('男人','女人'))   # 返回给定两个词语的相似度
# print(model.index_to_key)       # 返回列表，列表中的元素是词语
# print(model.key_to_index)    #  返回字典，key是词语，value是索引（index）
# print(model.vectors)    # 返回一个列表，列表中每个元素是一个向量列表
# print(len(model.vectors))    # 返回词向量的个数
# print(model.vector_size)    #  返回向量的维度

# model.add_vector("查通话记录",[])

url = 'http://douban.com'  # 要爬取的url页面
linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(url)
# print(html_text)
new_html_text  = text_transform(html_text)




title_and_keyword = ['日韩','勇士','爵士']
for word in title_and_keyword:
    # for k in seed_keywords.keys():
    for v in seed_keywords['personal_info']:
        print("%s和%s的相似度为%f"%(word,v,model.similarity(word,v)))

