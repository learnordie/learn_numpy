#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Numpy basic operations """

import numpy as np

a = np.array([[0,  1,  2,  3,  4],
              [5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])

print(a)
print("dimensions =", a.ndim)  # number of axes
print("shape =", a.shape)  # dimensions (size of the array in each dimension)
# total number of elements of the array
print("array size =", a.size, "elements")
print("data type =", a.dtype.name)  # name of the elements' data type
# size in bytes of each element of the array
print("item size =", a.itemsize, "bytes")
