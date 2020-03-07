import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist  # 加载图像库
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # 加载数据和标签;标签一般是数字
train_images = train_images/255  # 色度有255个值，除以255可以在训练中降低损失值
test_images = test_images/255

'''设置了一个三层的模型
第一层设置输入的形状为28*28，因为图片的像素是28
中间层即隐藏层设置了128个神经元
第三层有十个神经元，因为在数据集中有十个等级的衣服'''
model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),
                             tf.keras.layers.Dense(128, activation=tf.nn.relu),
                             tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

# print(train_images[0], train_labels[0])
# 训练模型
'''
model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy')
model.fit(train_images, train_labels, epochs=5)
# 测试
# model.evaluate(test_images, test_labels)
print(model.evaluate(test_images, test_labels))
'''


# 可以看到此时的损失和精确度仍然处于一个不太理想的数值

# 回调函数，主要用于判断当损失低于某个标准后自动停止循环
class Callback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('loss') < 0.4:
            print('ready to stop')
            self.model.stop_training = True


callbacks = Callback()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(train_images, train_labels, epochs=5, callbacks=[callbacks])
print(model.evaluate(test_images, test_labels))

