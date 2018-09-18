# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
Download MNIST dataset and Extract the gz files
"""
import patoolib #easy archive management
import requests
from tqdm import tqdm #progress bar

trlabURL = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
trimgURL = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
tslabURL = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
tsimgURL = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"

chunk_size=1024

################################################
r=requests.get(trlabURL, stream=True)

size=int(r.headers['content-length'])
filename=trlabURL.split ('/') [-1]

with open(filename, 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=size/chunk_size, unit='KB'):
        f.write(data)
        
print("Training labels are downloaded!")
patoolib.extract_archive(filename)
################################################
r=requests.get(trimgURL, stream=True)

size=int(r.headers['content-length'])
filename=trimgURL.split ('/') [-1]

with open(filename, 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=size/chunk_size, unit='KB'):
        f.write(data)
        
print("Training images are downloaded!")
patoolib.extract_archive(filename)
################################################
r=requests.get(tslabURL, stream=True)

size=int(r.headers['content-length'])
filename=tslabURL.split ('/') [-1]

with open(filename, 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=size/chunk_size, unit='KB'):
        f.write(data)
        
print("Testing labels are downloaded!")
patoolib.extract_archive(filename)
################################################
r=requests.get(tsimgURL, stream=True)

size=int(r.headers['content-length'])
filename=tsimgURL.split ('/') [-1]

with open(filename, 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=size/chunk_size, unit='KB'):
        f.write(data)
        
print("Testing images are downloaded!")
patoolib.extract_archive(filename)
################################################
