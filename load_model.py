import gensim

new_model = gensim.models.Word2Vec.load('model/gensim_w2v_sg0_model')  # 调用模型
print(type(new_model))
# sim_words = new_model.most_similar(positive=['女人'])
sim_words = new_model.wv.most_similar(positive=['女人'])   # 返回一个与给定词语最为相近的词语以及相似的的列表
# print(sim_words)
# for word, similarity in sim_words:
#     print(word, similarity)  # 输出’女人‘相近的词语和概率
print(new_model.wv.vectors)  # 返回结果是一个列表，列表中每个元素是每个词语表示的列表
print(new_model.wv.similarity('女人','女孩'))  # 返回结果为给定两个词语的相似度

print(new_model.vector_size)

print(new_model.wv)

print(new_model.seed)
