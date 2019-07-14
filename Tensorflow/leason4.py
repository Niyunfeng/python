import tensorflow as tf

state = tf.Variable(0, name='counter')
# print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

with tf.Session() as sses:
    sses.run(tf.global_variables_initializer())
    for _ in range(3):
        print(sses.run(update))
    print(sses.run(state))
    print(sses.run(new_value))
