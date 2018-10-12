# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
This code loads the model saved in ./model/ directory.
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

model=tf.keras.models.load_model(
    './model/model',
    custom_objects=None,
    compile=True
)
