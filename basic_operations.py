#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Basic operations with numpy arrays """

import numpy as np


a = np.array([20, 30, 40, 50])
b = np.arange(4)

# =========================== #
# Basic arithmetic operations #
# =========================== #

# Arithmetic operators on arrays apply elementwise
c = 5.4 * b
d = a - b
e = a * b
f = b / a

# If we try to divide by zero, we gat the following warning:
# "RuntimeWarning: divide by zero encountered in true_divide"
# and a "inf" value for that division
g = a/b

h = a < 35


# ======================= #
# Product of two matrices #
# ======================= #

# Unlike in many matrix languages, the product operator * operates elementwise
# in NumPy arrays. The matrix product can be performed using the @ operator
# (in python >=3.5) or the dot function or method:

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
C = A * B                       # elementwise product
D = A @ B                       # matrix product
E = A.dot(B)                    # another matrix product


# ================ #
# Basic statistics #
# ================ #

# Many unary operations, such as computing the sum of all the elements in the
# array, are implemented as methods of the ndarray class.

a = np.arange(0, 5.5, .5)
a_sum = a.sum()  # np.sum(a)
a_min = a.min()  # np.min(a)
a_max = a.max()  # np.max(a)
a_mean = a.mean()  # np.mean(a)
a_median = np.median(a)
a_std = a.std()  # np.std(a)
a_var = np.var(a)

print("sum =", a_sum)
print("min =", a_min)
print("max =", a_max)
print("mean =", a_mean)
print("median =", a_median)
print("std =", a_std)
print("variance =", a_var)

# By default, these operations apply to the array as though it were a list of
# numbers, regardless of its shape. However, by specifying the axis parameter
# you can apply an operation along the specified axis of an array:

b = np.arange(12).reshape(3, 4)
b_col_sum = b.sum(axis=0)  # sum of each column
b_row_min = b.min(axis=1)  # min of each row
b_row_cumsum = b.cumsum(axis=1)  # cumulative sum along each row

print()
print(b)
print("sum of each column =", b_col_sum)
print("min of each row =", b_row_min)
print("cumulative sum along each row =", b_row_cumsum)
