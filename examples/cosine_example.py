import numpy as np
import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pysim.distances import cosine

if __name__ == "__main__":
    a = np.array([1, 2, 43])
    b = np.array([3, 2, 1])

    cosine_dist = cosine(a, b)
    print('Cosine distance is : {}'.format(cosine_dist))