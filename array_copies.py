#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Arrays copies: same objects or new ones? """

import numpy as np


# ================================================ #
# "=" assignment: same object, same memory address #
# ================================================ #

a = np.random.randint(1, 100, 12).reshape(3, 4)
b = a  # no new object is created

print('\n"=" assignment:')
print('---------------')
print("Are 'a' and 'b' the same ndarray object?", b is a)
print("memory address of 'a' =", id(a))
print("memory address of 'b' =", id(b))

# So if I change something in b, it also changes in a
b[0, 0] = 999
print("Does a change in 'b' affects 'a'?", a[0, 0] == 999)
print("a[0,0] =", a[0, 0])

# And a change in the shape of b changes the shape of a
b.shape = 1, 12
print("Does a change in the shape of 'b' affects 'a'?", a.shape == b.shape)


# ============================================================= #
# "copy" method : different objects, different memory addresses #
# ============================================================= #

# The copy method makes a complete copy of the array and its data.

a = np.random.randint(1, 100, 12).reshape(3, 4)
b = a.copy()

print('\n"copy" method:')
print('--------------')
print("Are 'a' and 'b' the same ndarray object?", b is a)
print("memory address of 'a' =", id(a))
print("memory address of 'b' =", id(b))

# A change in b doesn't change a at all
b[0, 0] = 999
print("Does a change in 'b' affects 'a'?", a[0, 0] == 999)
print("a[0,0] =", a[0, 0])

# But changing the shape of b doesn't change the shape of a
b.shape = 1, 12
print("Does a change in the shape of 'b' affects 'a'?", a.shape == b.shape)


# ====================================================== #
# "view" method : different objects, same memory address #
# ====================================================== #

# Different array objects can share the same data. The view method creates a
# new array object that looks at the same data.

a = np.random.randint(1, 100, 12).reshape(3, 4)
b = a.view()

print('\n"view" method:')
print('--------------')
print("Are 'a' and 'b' the same ndarray object?", b is a)
print("memory address of 'a' =", id(a))
print("memory address of 'b' =", id(b))

# But, surprisingly, a change something in b changes a as well...
b[0, 0] = 999
print("Does a change in 'b' affects 'a'?", a[0, 0] == 999)
print("a[0,0] =", a[0, 0])

# But changing the shape of b doesn't change the shape of a
b.shape = 1, 12
print("Does a change in the shape of 'b' affects 'a'?", a.shape == b.shape)
