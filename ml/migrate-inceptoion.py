from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


local_weights_file = 'inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
# 实例化对象
pre_trained_model = InceptionV3(input_shape=(150, 150, 3),
                                include_top=False,   # 忽略顶层直接进入卷积
                                weights=None)
pre_trained_model.load_weights(local_weights_file)

for layer in pre_trained_model.layers:  # 遍历图层并锁定
    layer.trainable = False
last_layer = pre_trained_model.get_layer('mixed7')
last_output = last_layer.output
# print(pre_trained_model.summary())

x = layers.Flatten()(last_output)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dropout(0.2)(x)  # 去掉20%的神经元，可以修复过度拟合
x = layers.Dense(1, activation='sigmoid')(x)

model = Model(pre_trained_model.input, x)
model.compile(optimizer=RMSprop(lr=0.0001),
              loss='binary_crossentropy',
              metrics=['acc'])

train_datagen = ImageDataGenerator(rescale=1 / 255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
trian_generator = train_datagen.flow_from_directory('cats_and_dogs_filtered/train',  # 主目录
                                                    target_size=(150, 150),
                                                    batch_size=20,
                                                    class_mode='binary')

validation_datagen = ImageDataGenerator(rescale=1 / 255)
validation_generator = validation_datagen.flow_from_directory('cats_and_dogs_filtered/validation',
                                                              target_size=(150, 150),
                                                              batch_size=32,
                                                              class_mode='binary')

history = model.fit_generator(trian_generator, steps_per_epoch=100, epochs=20,
                              validation_data=validation_generator, validation_steps=50)
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epoches = range(len(acc))
plt.plot(epoches, acc, 'r')
plt.plot(epoches, val_acc, 'b')
plt.legend(loc=0)
plt.figure()
plt.show()


