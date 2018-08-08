#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Numpy basic operations """

import numpy as np

a = np.array([[0,  1,  2,  3,  4],
              [5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])

print(a)
print()

# number of axes
print("dimensions =", a.ndim)

# size of the array in each dimension
nrows, ncols = a.shape
print("# of rows =", nrows)
print("# of columns =", ncols)
print("shape =", a.shape)

# total number of elements of the array
print("array size =", a.size, "elements")

# data type name of the elements of the array
print("data type =", a.dtype.name)

# size in bytes of each element of the array
print("item size =", a.itemsize, "bytes")
