# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
Import MNIST dataset
Based on
https://medium.com/@mannasiladittya/converting-mnist-data-in-idx-format-to-python-numpy-array-5cb9126f99f1
"""
#import os
import struct as st
import numpy as np
#import patoolib #easy archive management
#import gzip
#import urllib
#import requests
#from tqdm import tqdm #progress bar
#import os

#Creating a dictionary: images->train-images.idx3-ubyte && labels->train-labels.idx1-ubyte
filename = {'images' : 'train-images.idx3-ubyte' ,'labels' : 'train-labels.idx1-ubyte'}

train_imagesfile = open(filename['images'],'rb')#Read, Binary

train_imagesfile.seek(0)#seek() sets file's current position
#seek(0): Absolute #seek(1): Relative to Current #seek(2): Relative to End

#struct.unpack(format, buffer)
#>:big-endian #B: unsigned char(integer) size: 1 Byte
magic = st.unpack('>4B',train_imagesfile.read(4))

#I: unsigned int (4Bytes)
nImg = st.unpack('>I',train_imagesfile.read(4))[0] #num of images [0] makes it int
#without [0] it is tuple
nR = st.unpack('>I',train_imagesfile.read(4))[0] #num of rows
nC = st.unpack('>I',train_imagesfile.read(4))[0] #num of column

#Declare Image NumPy array (Optional, not required in this case)
images_array = np.zeros((nImg,nR,nC))#uImg, nR, and nC must be int

nBytesTotal = nImg*nR*nC*1 #since each pixel data is 1 byte
#'>'+'B'*nBytesTotal,train_imagesfile.read(nBytesTotal)-> reads all the data
#without reshape it is a vector of size 47040000(nBy)tesTotal
images_array = np.asarray(st.unpack('>'+'B'*nBytesTotal,train_imagesfile.read(nBytesTotal))).reshape((nImg,nR,nC))
train_imagesfile.close



