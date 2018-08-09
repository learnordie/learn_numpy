#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Stacking arrays together """

import numpy as np

a = np.random.randint(0, 100, 4).reshape(2, 2)
b = np.random.randint(0, 100, 4).reshape(2, 2)

print("a =")
print(a)
print()
print("b =")
print(b)
print()

# ============================= #
# Basic methods to stack arrays #
# ============================= #

c = np.vstack((a, b))  # stack arrays as new rows
d = np.hstack((a, b))  # stack arrays as new columns

print("c =")
print(c)
print()
print("d =")
print(d)
print()


# ===================== #
# More advanced options #
# ===================== #

# For two-dimensional arrays, "column_stack" is equivalent to "hstack":
e = np.column_stack((a, b))
print("e =")
print(e)
print()

# But for one-dimensional arrays, they are not, the results are different:
v1 = np.random.randint(1, 100, 3)
v2 = np.random.randint(1, 100, 3)

print("v1 =")
print(v1)
print()
print("v2 =")
print(v2)
print()

f = np.column_stack((v1, v2))
g = np.hstack((v1, v2))

print("f =")
print(f)
print()
print("g =")
print(g)
print()


# On the other side, "row_stack" is equivalent to "vstack" for any input arrays
# (one-dimensional or multidimensional):

h = np.row_stack((a, b))
print("h =")
print(h)
print()

i = np.row_stack((v1, v2))
j = np.vstack((v1, v2))

print("i =")
print(i)
print()
print("j =")
print(j)
print()
