import tensorflow_datasets as tfds
import numpy
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import io

imdb, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
train_data, test_data = imdb['train'], imdb['test']
train_sentences, train_labels, test_sentences, test_labels = [], [], [], []
for s, l in train_data:
    train_sentences.append(str(s.numpy()))
    train_labels.append(l.numpy())
for s, l in test_data:
    test_sentences.append(str(s.numpy()))
    test_labels.append(l.numpy())

train_labels_final = numpy.array(train_labels)
test_labels_final = numpy.array(test_labels)

vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type = 'post'
oov_tok = '<oov>'

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_sentences)
word_index = tokenizer.word_index
sequence = tokenizer.texts_to_sequences(train_sentences)
padded = pad_sequences(sequence, maxlen=max_length, truncating=trunc_type)

testing_seq = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(testing_seq, maxlen=max_length)

model = tf.keras.Sequential([tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),  # 嵌入
                             tf.keras.layers.Flatten(),
                             tf.keras.layers.Dense(6, activation='relu'),
                             tf.keras.layers.Dense(1, activation='sigmoid')])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
model.fit(padded, train_labels_final, epochs=5, validation_data=(test_padded, test_labels_final))
reverse = dict([(value, key) for (key, value) in word_index.items()])

with io.open('meta.tsv', 'w', encoding='utf-8') as out_m:
    for word_num in range(1, vocab_size):
        word = reverse[word_num]
        out_m.write(word + '\n')
weights = model.layers[0].get_weights()[0]
with io.open('vecs.tsv', 'w', encoding='utf-8') as out_v:
    for word_num in range(1, vocab_size):
        embedding = weights[word_num]
        out_v.write('\t'.join([str(x) for x in embedding]) + '\n')
