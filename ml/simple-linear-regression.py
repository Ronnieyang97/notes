# 简单的线性回归预测
import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
# 设置优化器为随机梯度下降，损失函数为平均平方误差
xs = np.array([-1, 0, 1, 2, 3, 4], dtype=float)
ys = np.array([-3, -1, 1, 3, 5, 7], dtype=float)

model.fit(xs, ys, epochs=500)  # epochs参数表示循环次数

print(model.predict([10]))  # 表示当x输入为10时，预测y的输出
