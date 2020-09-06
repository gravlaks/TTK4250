#!/bin/bash
"""
File name: np_arrays.py

Creation Date: So 06 Sep 2020 

Description:

"""

# Standard Python Libraries
# -----------------------------------------------------------------------------------------
import numpy as np

# Local Application Modules
# -----------------------------------------------------------------------------------------

a = np.arange(15).reshape(3, 5)
print(a)
b = np.array([23, 42.1, 4])
print(b)
print(b.dtype.name)

complex_array = np.array([ [1, 2], [3, 5]], dtype=complex)
print(complex_array)

array_2d = np.arange(0, 20, 2).reshape(2, 5)
print(array_2d)


matrix_a = np.array([[1,2], [2,1]])
matrix_b = np.array([[-1, 2], [2, -1]])

print(matrix_a@matrix_b)
r_n_g = np.random.default_rng(2)
print(r_n_g.random((2,3)))
