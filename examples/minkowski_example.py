"""
    author: Durgesh Samariya
    email: samariya.durgesh@gmail.com
    Licence: BSD 2 clause
    Description: Example of using Minkowski distance measure.
"""

import numpy as np
import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pysim is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pysiml.distances import minkowski

if __name__ == "__main__":
    a = np.array([1, 2, 43])
    b = np.array([3, 2, 1])

    minkowski_dist = minkowski(a, b, 2)
    print('Minkowski distance is : {}'.format(minkowski_dist))