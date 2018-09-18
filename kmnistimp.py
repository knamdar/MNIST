# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
Import MNIST dataset
Based on
https://medium.com/@mannasiladittya/converting-mnist-data-in-idx-format-to-python-numpy-array-5cb9126f99f1
"""
import struct as st
import numpy as np




#Creating a dictionary: images->train-images.idx3-ubyte && labels->train-labels.idx1-ubyte
filename = {'trimg' : 'train-images.idx3-ubyte' ,'trlab' : 'train-labels.idx1-ubyte'
            ,'tslab' : 't10k-labels.idx1-ubyte', 'tsimg' : 't10k-images.idx3-ubyte'}

def kmnist_imp_img(tt):
    #filename = {'trimg' : 'train-images.idx3-ubyte' ,'labels' : 'train-labels.idx1-ubyte'}
    current_file = open(filename[tt+"img"],'rb')#Read, Binary

    current_file.seek(0)#seek() sets file's current position
    #seek(0): Absolute #seek(1): Relative to Current #seek(2): Relative to End

    #struct.unpack(format, buffer)
    #>:big-endian #B: unsigned char(integer) size: 1 Byte
    magic = st.unpack('>4B',current_file.read(4))

    #I: unsigned int (4Bytes)
    nImg = st.unpack('>I',current_file.read(4))[0] #num of images [0] makes it int
    #without [0] it is tuple
    nR = st.unpack('>I',current_file.read(4))[0] #num of rows
    nC = st.unpack('>I',current_file.read(4))[0] #num of column

    #Declare Image NumPy array (Optional, not required in this case)
    #images_array = np.zeros((nImg,nR,nC))#uImg, nR, and nC must be int

    nBytesTotal = nImg*nR*nC*1 #since each pixel data is 1 byte
    #'>'+'B'*nBytesTotal,current_file.read(nBytesTotal)-> reads all the data
    #without reshape it is a vector of size 47040000(nBy)tesTotal
    images_array = np.asarray(st.unpack('>'+'B'*nBytesTotal,current_file.read(nBytesTotal)),dtype='uint8').reshape((nImg,nR,nC))
    current_file.close
    return images_array
###################################################
def kmnist_imp_lab(tt):
    #filename = {'trimg' : 'train-images.idx3-ubyte' ,'labels' : 'train-labels.idx1-ubyte'}
    current_file = open(filename[tt+"lab"],'rb')#Read, Binary

    current_file.seek(0)#seek() sets file's current position
    #seek(0): Absolute #seek(1): Relative to Current #seek(2): Relative to End

    #struct.unpack(format, buffer)
    #>:big-endian #B: unsigned char(integer) size: 1 Byte
    magic = st.unpack('>4B',current_file.read(4))

    #I: unsigned int (4Bytes)
    nR = st.unpack('>I',current_file.read(4))[0] #num of rows
    
    #Declare Image NumPy array (Optional, not required in this case)
    images_array = np.zeros((nR),dtype='uint8')#uImg, nR, and nC must be int

    nBytesTotal = nR*1 #since each pixel data is 1 byte
    #'>'+'B'*nBytesTotal,current_file.read(nBytesTotal)-> reads all the data
    #without reshape it is a vector of size 47040000(nBy)tesTotal
    images_array = np.asarray(st.unpack('>'+'B'*nBytesTotal,current_file.read(nBytesTotal)),dtype='uint8').reshape((nR))
    current_file.close
    return images_array
######################################################
x_train=kmnist_imp_img('tr')
y_train=kmnist_imp_lab('tr')
x_test=kmnist_imp_img('ts')
y_test=kmnist_imp_lab('ts')

