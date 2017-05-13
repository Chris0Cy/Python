import tensorflow as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

z = 3*(tf.pow(y,2))+(2*x*y)+5*(tf.pow(x,2))-6

s = tf.Session()
print(s.run(z, {x:3.2, y:9.1}))   
print(s.run(z, {x:4.4, y:10.2}))