import cv2
import tensorflow as tf
import numpy

model = tf.keras.models.load_model('horseorhuman.h5')

for i in range(4):
    img = cv2.imread('test/{}.jpg'.format(i))
    images = cv2.resize(img, (300, 300))
    x = numpy.expand_dims(images, axis=0)  # 改变数组维度以适应predict
    classes = model.predict(x, batch_size=10)
    if classes[0] > 0.5:
        print('{}is a human'.format(i))
    else:
        print('{}is a horse'.format(i))
