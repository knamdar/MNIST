# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca

Based on 
https://www.tensorflow.org/tutorials/#deep-mnist-for-experts
"""


import tensorflow as tf
###############################################
#these two lines can be used to import data
#However, kmnistimp.py is written to do the task

#mnist = tf.keras.datasets.mnist
#
#(x_train, y_train),(x_test, y_test) = mnist.load_data()
###############################################
x_train, x_test = x_train / 255.0, x_test / 255.0

#drawing the nn
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

#opting the training algorithm
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#train the network
model.fit(x_train, y_train, epochs=5)

#save the model including optimizer and weights
tf.keras.models.save_model(
    model,
    './model2/model2',
    overwrite=True,
    include_optimizer=False
)

#evaluation can be done using the following line, if it is essential
#model.evaluate(x_test, y_test)

# Launch the graph in a session.
sess = tf.Session()

# Create a summary writer, add the 'graph' to the event file.
writer = tf.summary.FileWriter('./logs2/', sess.graph)
