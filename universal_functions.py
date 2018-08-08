#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" "Universal functions" with numpy arrays """

import numpy as np

# NumPy provides familiar mathematical functions such as sin, cos, and exp.
# In NumPy, these are called  universal functions(ufunc). Within NumPy, these
# functions operate elementwise on an array, producing an array as output.

A = np.arange(3)
B = np.exp(A)
C = np.sqrt(A)
D = np.add(B, C)

print(A)
print(B)
print(C)
print(D)
