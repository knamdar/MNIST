# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
find 10 robust incidents of 2
"""
import numpy as np
#import matplotlib.pyplot as plt
#import imageio
#import copy

#test=x_test[1]
#test will be 28*28 but model.evaluate needs 3 dimentions
#test2 = np.expand_dims(test, axis=0) 
#test2 can be passed to the model
count=0;
ind=[]#index of dataset starts from zero
info=np.zeros((10,3),dtype=float)
for i in range(y_test.size):
    if y_test[i,0]==2:
        #print(i)
        loss, acc=model.evaluate(np.expand_dims(x_test[i], axis=0), np.expand_dims(y_test[i,0], axis=0))
        if acc==1:
            info[count][0]=i
            info[count][1]=loss
            info[count][2]=acc
            count=count+1
            ind.append(i)
    if count==10:
        break
