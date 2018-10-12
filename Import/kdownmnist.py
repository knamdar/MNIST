# -*- coding: utf-8 -*-
"""
@author: Khashayar Namdar
knamdar@uwo.ca
Download and Extract mnist
"""
import patoolib #easy archive management
from kdown import kdown#file not file.py

trlabURL = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
trimgURL = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
tslabURL = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
tsimgURL = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"

f=kdown(trlabURL)
patoolib.extract_archive(f)

f=kdown(trimgURL)
patoolib.extract_archive(f)

f=kdown(tslabURL)
patoolib.extract_archive(f)

f=kdown(tsimgURL)
patoolib.extract_archive(f)
