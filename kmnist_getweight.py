# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
get weights of the saved model
"""
import h5py
#import tensorflow as tf
import copy
import numpy as np

#for weights that are going to be extracted from the traditionally saved models
#with tf.variable_scope("None", reuse=True): 
#    w = tf.get_variable('dense_12/kernel:0')
#    print(w.eval())
#saver = tf.train.Saver()
#sess = tf.Session()
#sess.run(tf.global_variables())
#saver.save(sess, './model/my_test_model')

###for weights that are going to be extracted from single-file model
f = h5py.File('./model/model', 'r')
#list(f)
#list(f['model_weights'])
dense_12w=copy.copy(np.transpose(f['model_weights/dense_12/dense_12/kernel:0'].value))
dense_12b=copy.copy(f['model_weights/dense_12/dense_12/bias:0'].value)
dense_13w=copy.copy(np.transpose(f['model_weights/dense_13/dense_13/kernel:0'].value))
dense_13b=copy.copy(f['model_weights/dense_13/dense_13/bias:0'].value)