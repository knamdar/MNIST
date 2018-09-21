# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
creating delta images
"""

import numpy as np
import matplotlib.pyplot as plt

#dense_12w=np.transpose(dense_12w)
#dense_13w=np.transpose(dense_13w)
weffective=np.matmul(dense_13w,dense_12w)
a=np.max(weffective[6][:])
#print(weffective[6])
b=np.argmax(weffective[6][:])
bsixmaking=np.zeros((28,28))
#bsixmaking[1][(b%28)-1]=40     #working with just one pixel
bsixmaking[int(np.floor(b/28))][(b%28)-1]=20

wholesgn=np.sign(weffective)
sixmaking=wholesgn[6][:]
"""
sixmaking=np.zeros((784,1))
for i in range(784):
    if wholesgn[6][i]==1:
        sixmaking[i][0]=1
"""

#test=x_test[ind[9]]
#test2=np.reshape(test,(1,784))
#test2=np.reshape(test,(28,28))

sixmaking=np.reshape(sixmaking,(28,28))
plt.imshow(sixmaking)
#test2=test+0.22*sixmaking
#test2=(test2-np.min(test2))
#test2=test2/np.max(test2)
#model.predict(np.expand_dims(sixmaking, axis=0))
#plt.imshow(test2)