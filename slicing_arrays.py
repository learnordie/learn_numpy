#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Indexing and slicing numpy arrays """

import numpy as np


# ===================== #
# Indexing numpy arrays #
# ===================== #

a = np.arange(12)**3

print(a)
print()
print("a1 =", a[0])
print("a2 =", a[1])
print("a3 =", a[2])
print("...")
print("a10 =", a[9])
print("a11 =", a[10])
print("a12 =", a[11])


b = np.reshape(a, (3, 4))

print()
print(b)
print()
print("b11 =", b[0, 0])
print("b12 =", b[0, 1])
print("b13 =", b[0, 2])
print("b14 =", b[0, 3])
print()
print("b21 =", b[1, 0])
print("b22 =", b[1, 1])
print("b23 =", b[1, 2])
print("b24 =", b[1, 3])
print()
print("b31 =", b[2, 0])
print("b32 =", b[2, 1])
print("b33 =", b[2, 2])
print("b34 =", b[2, 3])


# ==================================== #
# Slicing one-dimensional numpy arrays #
# ==================================== #

c1 = a[:5]  # from index = 0 to index = 4
c2 = a[5:]  # from index = 5 to index = end
c3 = a[2:5]  # from index = 2 to index = 4
print()
print("a =", a)
print()
print("a[:5] =", c1)
print("a[5:] =", c2)
print("a[2:5] =", c3)


c4 = a[::3]  # from start to end, select every 3rd element
c5 = a[:5:2]  # from start to index = 4, select every 2nd element
print()
print("a[::3] =", c4)
print("a[:5:2] =", c5)

c6 = a[::-1]  # reverse an array
print()
print("a[::-1] =", c6, "(reversed array)")


# ====================================== #
# Slicing multi-dimensional numpy arrays #
# ====================================== #

# Multidimensional arrays can have one index per axis.

nrows, ncols = b.shape

print()
print(b)
print()
print("# of rows =", nrows)
print("# of columns =", ncols)


row1 = b[0, :]
row2 = b[1, :]
row3 = b[2, :]

column1 = b[:, 0]
column2 = b[:, 1]
column3 = b[:, 2]
column4 = b[:, 3]

print()
print("row1 =", row1)
print("row2 =", row2)
print("row3 =", row3)

print()
print("column1 =", column1)
print("column2 =", column2)
print("column3 =", column3)
print("column4 =", column4)
