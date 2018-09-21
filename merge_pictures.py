# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
merge original exampkes, delta, and adversarial pictures in 10 rows and 3 columns
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio
import copy

k=ind.pop(0)
merged=copy.copy(x_test[k])
for i in ind:
    #print(i)
    merged=np.concatenate((merged, x_test[i]), axis=0)#axis=1-->put images horizontally
#axis=0-->put together vertically 
ind.insert(0,k)
plt.imshow(merged)
imageio.imwrite('outfile.jpg', merged)
################################################
k=ind.pop(0)
merged2=copy.copy(0.22*sixmaking)
for i in ind:
    #print(i)
    merged2=np.concatenate((merged2, 0.22*sixmaking), axis=0)#axis=1-->put images horizontally
#axis=0-->put together vertically 
ind.insert(0,k)
plt.imshow(merged2)
imageio.imwrite('outfile2.jpg', merged2)
###############################################
k=ind.pop(0)
test2=x_test[k]+0.22*sixmaking
test2=(test2-np.min(test2))
test2=test2/np.max(test2)
merged3=copy.copy(test2)
print(model.predict_classes(np.expand_dims(test2, axis=0))[0])
for i in ind:
    test2=x_test[i]+0.22*sixmaking
    test2=(test2-np.min(test2))
    test2=test2/np.max(test2)
    print(model.predict_classes(np.expand_dims(test2, axis=0))[0])
    #print(i)
    merged3=np.concatenate((merged3, test2), axis=0)#axis=1-->put images horizontally
#axis=0-->put together vertically 
ind.insert(0,k)
plt.imshow(merged3)
imageio.imwrite('outfile3.jpg', merged3)
###################################################
merged4=np.concatenate((merged, merged2), axis=1)
merged4=np.concatenate((merged4, merged3), axis=1)
plt.imshow(merged4)
imageio.imwrite('outfile4.jpg', merged4)