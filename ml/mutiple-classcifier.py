from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

train_datagen = ImageDataGenerator(rescale=1 / 255,
                                   rotation_range=40,  # 随机旋转0-40（最高180）
                                   width_shift_range=0.2,  # 类似滑动窗口，20%
                                   height_shift_range=0.2,
                                   shear_range=0.2,  # 剪切，并随机分配到图像中指定的部分
                                   zoom_range=0.2,  # 缩放
                                   horizontal_flip=True,  # 水平翻转
                                   fill_mode='nearest'  # 填充模式
                                   )  # 完成了图像增强
trian_generator = train_datagen.flow_from_directory('rps/rps',  # 主目录
                                                    target_size=(150, 150),
                                                    class_mode='categorical')  # 分类模式
validation_datagen = ImageDataGenerator(rescale=1 / 255)
validation_generator = validation_datagen.flow_from_directory('rps/rps-test-set',
                                                              target_size=(150, 150),
                                                              class_mode='categorical')

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(64, (3, 3), activation='relu',
                                                           input_shape=(150, 150, 3)),  # 输入颜色为三种
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    # 顶部有4层卷积层
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dropout(0.5),
                                    tf.keras.layers.Dense(512, activation='relu'),
                                    tf.keras.layers.Dense(3, activation='softmax')  # 3个神经元，softmax适用于多元分类
                                    ])
model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.RMSprop(lr=0.001), metrics=['acc'])
# 损失函数为多元交叉熵，优化器使用RMS（可调整学习效率），度量标准为准确率
history = model.fit_generator(trian_generator, epochs=25, validation_data=validation_generator)

model.save('rps.h5')

