#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Iterating over multi-dimensional arrays """

import numpy as np

a = np.random.random_integers(0, 100, 15).reshape(5, 3)

print(a)


# ========================== #
# Rows and columns iteration #
# ========================== #

# Iterating over multidimensional arrays is always done with respect to the
# first axis. So we can access the rows directly:

print()
print("Rows:")
for row in a:
    print("\t", row)


# To get access to the columns, we can iterate over the transpose of the
# original multidimensional array:

print()
print("Columns:")

for column in a.T:  # iteration over the transpose of "a"
    print("\t", column)


# ================= #
# Element iteration #
# ================= #

# However, if one wants to perform an operation on each element in the array,
# one can use the flat attribute which is an iterator over all the elements of
# the array:

print()
print("Elements:")
print("\t", end="")

for element in a.flat:
    print(element, end="; ")

print("\n")
