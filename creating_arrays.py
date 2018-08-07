#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" How to create numpy arrays """

import numpy as np

# a = np.array(1, 2, 3, 4)  # wrong!
a = np.array([1, 2, 3, 4])  # right!

b = np.array([(1.5, 2, 3), (4, 5, 6)])

# the type of the array can also be explicitly specified at creation time
c = np.array([[1, 2], [3, 4]], dtype=complex)


# Often, the elements of an array are originally unknown, but its size is
# known. Hence, NumPy offers several functions to create arrays with initial
# placeholder content. These minimize the necessity of growing arrays, an
# expensive operation.

zeros = np.zeros((3, 4), dtype=np.int16)
ones = np.ones((3, 4), dtype=np.int16)
random1 = np.empty((6, 6), dtype=np.int16)
random2 = np.empty((2, 9), dtype=np.float32)

print(zeros)
print(ones)
print(random1)
print(random2)


# To create sequences of numbers, NumPy provides a function analogous to range
# that returns arrays instead of lists.
seq1 = np.arange(10, 30, 5, dtype=np.int32)  # start, stop, step, data type
print(seq1)

# np.arange accepts float arguments, but in that case it is generally not
# possible to predict the number of elements obtained, due to the finite
# floating point precision. For this reason, it is usually better to use the
# function linspace that receives as an argument the number of elements that
# we want, instead of the step.

# start, stop, number of elements, dtype
seq2 = np.linspace(0, 2, 9,  dtype=np.float32)
print(seq2)

# np.linspace is very  useful to evaluate function at lots of points
from numpy import pi
import matplotlib.pyplot as plt
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)
# plt.plot(f)
# plt.show()

array1 = np.arange(0, 10, .5)
print('Before using the "reshape" method of ndarray objects:')
print(array1)
array1.reshape(2, 10)  # as we will see, that method doesn't change the object
print('After using the "reshape" method of ndarray objects:')
print(array1)
array2 = np.reshape(array1, (4, 5))  # creates a new object
print('After using the "reshape" numpy function:')
print(array2)
