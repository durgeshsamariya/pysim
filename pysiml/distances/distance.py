import numpy as np

def cosine(a, b):
    return 1 - np.dot(a, b) / (np.sqrt(np.dot(a, a)) * np.sqrt(np.dot(b, b)))
    
def euclidean(a, b):
    return np.sqrt(np.sum(np.dot((a - b), (a - b))))

def jaccard(a, b):
    return np.double(np.bitwise_and((a != b), np.bitwise_or(a != 0, b != 0)).sum()) / np.double(np.bitwise_or(a != 0, b != 0).sum())

def mahalanobis(a, b, vi):
    return np.sqrt(np.dot(np.dot((a - b), vi),(a - b).T))
    
def manhattan(a, b):
    return np.sum(np.fabs(a - b))

def minkowski(a, b, p):
    return np.power(np.sum(np.power(np.fabs(a - b), p)), 1 / p)