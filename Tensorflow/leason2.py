import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float)
y_data = 0.1 * x_data + 0.3

# create tensorflow structure start
Weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
Biases = tf.Variable(tf.zeros([1]))
y = Weight * x_data + Biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
# create tensorflow structure end

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(501):
        sess.run(optimizer)
        if step % 20 == 0:
            print(step, sess.run(Weight), sess.run(Biases), sess.run(loss))
