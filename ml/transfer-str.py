from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences  # 填充功能
import json

sentences = ['I love my dog', 'I love my cat', 'you love my dog!', 'do you love my dogs?']

token = Tokenizer(num_words=100, oov_token='<oov>')  # oov_token在遇到语料库中不存在的单词设为<oov>
token.fit_on_texts(sentences)  # 对sentences中的对象逐个拆分单词，并构建字典
word_index = token.word_index
sequences = token.texts_to_sequences(sentences)  # 通过已构建的字典将单词转化为数字
testdata = ['i really love my dog']
test_seq = token.texts_to_sequences(testdata)  # 此时的结果会被是i love my dog对应的数组，因为really不在语料库中
pad = pad_sequences(sequences, padding='post', truncating='post', maxlen=5)
# 以0填充缺失，默认向前填充，将padding设为post后则在后填充,truncating设置当数组长度超过maxlen时，向后截断或向前阶段

with open('sarcasm.json', 'r') as f:
    datastore = json.load(f)
sentences, labels, urls = [], [], []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

tokenizer = Tokenizer(oov_token='<oov>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')

