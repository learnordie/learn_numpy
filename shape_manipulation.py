#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Changing the shape of an array """

import numpy as np

a = np.random.randint(0, 100, 12).reshape(4, 3)

# =================== #
# Most common methods #
# =================== #

# To convert a multidimensional array in a one-dimensional array
# We can not use "a.flat" because that is an iterator, not a function.
# So we use the method "ravel" instead:
b = a.ravel()  # returns the array, flattened
print(b)
print()

# The method "reshape" returns a new array with a modified shape:
c = a.reshape(6, 2)
print(c)
print()

# If a dimension is given as -1 in a reshaping operation,
# the other dimensions are automatically calculated:
d = a.reshape(3, -1)  # this will result in a (3, 4) array
print(d)
print()


# ===================================================== #
# Methods to avoid (or, at least, be very careful with) #
# ===================================================== #

# The method "resize" modifies the array itself:
a.resize(6, 2)
print(a)
print()

# So be very very careful when using the method "resize",
# because an expression like "e = a.resize(1, 12)" does not work the way we
# might expect (it changes the shape of "a" and returns "None").
e = a.resize(1, 12)
print(e)
print()
print(a)
print()
