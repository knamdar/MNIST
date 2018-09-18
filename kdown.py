# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
Download files from internet
input=URL
output=filename (last part of the URL)
It also downloads the file to the WD
"""


import requests
from tqdm import tqdm #progress bar

def kdown(URL):
    chunk_size=1024
    r=requests.get(URL, stream=True)

    size=int(r.headers['content-length'])
    filename=URL.split ('/') [-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=size/chunk_size, unit='KB'):
            f.write(data)
        
        print("{} is downloaded!".format(filename))

    return filename