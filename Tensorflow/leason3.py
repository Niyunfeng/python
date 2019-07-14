import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])

# matrix multiply
product = tf.matmul(matrix1, matrix2)

# session method 1
sess = tf.Session()
print(sess.run(product))
sess.close()

# session method 2
with tf.Session() as sess:
    print(sess.run(product))
