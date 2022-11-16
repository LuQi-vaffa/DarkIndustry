import gensim
from gensim.models.word2vec import Word2Vec

# 读取数据，用gensim中的word2vec训练词向量
file = open("dataset/text/text.txt",encoding="utf-8")
sss = []

def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())

while  True:
    # Get next line from file
    line  =  file.readline()
    # If line is empty then end of file reached
    if  not  line  :
        break
    if line != "\n":
        ss = line.strip()
        s1 = remove_upprintable_chars(ss)
        s2 = s1.split(" ")
        s3 = [x.strip() for x in s2 if x.strip() != '']
        print(s3)
        sss.append(s3)
file.close()

# while True:
#     ss = file.readline().replace('\n', '').rstrip()
#     if ss:
#         # s1 = ss.split(" ")
#         # sss.append(s1)
#         print(ss)
#     else:
#         break
# file.close()


model = Word2Vec(vector_size=200, workers=5, sg=1,min_count=5)  # 生成词向量为200维，考虑上下5个单词共10个单词，采用sg=1的方法也就是skip-gram
model.build_vocab(sss)
model.train(sss, total_examples=model.corpus_count,epochs=model.epochs)
model.save('./model/gensim_w2v_sg0_model')  # 保存模型


