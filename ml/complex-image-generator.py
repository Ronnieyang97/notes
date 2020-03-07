from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

train_datagen = ImageDataGenerator(rescale=1 / 255)
trian_generator = train_datagen.flow_from_directory('horse-or-human',  # 主目录
                                                    target_size=(300, 300),
                                                    batch_size=128,
                                                    class_mode='binary')
validation_datagen = ImageDataGenerator(rescale=1 / 255)
validation_generator = validation_datagen.flow_from_directory('validation-horse-or-human',
                                                              target_size=(300, 300),
                                                              batch_size=32 ,
                                                              class_mode='binary')
'''test_datagen = ImageDataGenerator(rescale=1 / 255)
validation_generator = test_datagen.flow_from_directory(test_dir,
                                                        target_size=(300, 300),
                                                        batch_size=32,
                                                        class_mode='binary')'''
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu',
                                                           input_shape=(300, 300, 3)),  # 输入颜色为三种
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    # 顶部有5层卷积层
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512, activation='relu'),
                                    tf.keras.layers.Dense(1, activation='sigmoid')  # 单个神经元，sigmoid针对二元分类
                                    ])
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.RMSprop(lr=0.001), metrics=['acc'])
# 损失函数为二元交叉熵，优化器使用RMS（可调整学习效率），度量标准为准确率
history = model.fit_generator(trian_generator, steps_per_epoch=8, epochs=15,
                              validation_data=validation_generator, validation_steps=8)
# step_per_epoch取决于train_generator中batch_size的大小，图片总量/batch_size的大小，validation_steps同理，verbose控制输出行数

model.save('horseorhuman.h5')
