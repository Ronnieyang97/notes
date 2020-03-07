import tensorflow as tf
fashion_mnist = tf.keras.datasets.fashion_mnist  # 加载图像库
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # 加载数据和标签;标签一般是数字
train_images = train_images.reshape(60000, 28, 28, 1)/255  # 色度有255个值，除以255可以在训练中降低损失值
test_images = test_images.reshape(10000, 28, 28, 1)/255


model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    # 64个过滤器，大小为3*3，激活为relu（即负值），大小为28*28，用一个字节表示颜色深度（灰色）
    tf.keras.layers.MaxPool2D(2, 2),
    # 2*2池，即在2*2的方格内选用数值最大的值作为这四个格子的值
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    # 第二层卷积层
    # 通过两层卷积的操作做到很大程度的简化
    tf.keras.layers.Flatten(),  # 平坦层
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(train_images, train_labels, epochs=5)
print(model.evaluate(test_images, test_labels))
