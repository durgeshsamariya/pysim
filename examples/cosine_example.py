"""
    author: Durgesh Samariya
    email: samariya.durgesh@gmail.com
    Licence: BSD 2 clause
    Description: Example of using Cosine distance measure.
"""

import numpy as np
import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pysim is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pysim.distances import cosine

if __name__ == "__main__":
    a = np.array([1, 2, 43])
    b = np.array([3, 2, 1])

    cosine_dist = cosine(a, b)
    print('Cosine distance is : {}'.format(cosine_dist))