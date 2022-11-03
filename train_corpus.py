import gensim
from gensim.models.word2vec import Word2Vec

# 读取数据，用gensim中的word2vec训练词向量
file = open(r"C:\Users\Lu\Documents\Tencent Files\1344692870\FileRecv\text.txt",encoding='utf-8')
sss = []
while True:
    ss = file.readline().replace('\n', '').rstrip()
    if ss == '':
        break
    s1 = ss.split(" ")
    sss.append(s1)
file.close()
model = Word2Vec(vector_size=200, workers=5, sg=1)  # 生成词向量为200维，考虑上下5个单词共10个单词，采用sg=1的方法也就是skip-gram
model.build_vocab(sss)
model.train(sss, total_examples=model.corpus_count,epochs=model.epochs)
model.save('./model/gensim_w2v_sg0_model')  # 保存模型


