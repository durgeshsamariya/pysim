# Python Similarity Measure (PySIM)
PySIM is a python library for evaluate distance between two vectors. PySIM includes more than five similarity measure.

# Installation
It is highly recommended to use **pip** for installation.

```
pip install pysim
```

You can install PySIM by clonning the repo
```
git clone https://github.com/durgeshsamariya/pysim.git
cd pysim
pip install .
```
**Required Dependencies:**
- Python 3.5, 3.6 or 3.7
- numpy >= 1.13

## Supported similarity measures
- Euclidean distance
- Cosine distance
- Jaccard distance
- Mahalanobis distance
- Manhattan distance
- Minkowski distance

The list of distance measures, their fuction and the mathematical equations are listed below.

| Name                 |  Function                  | Equation     |
| -------------------- | -------------------------- | --------------------|
|  Euclidean           |  `euclidean(a, b)`         | `sqrt(sum((a - b)^ 2))` |
|  Cosine              |  `cosine(a, b)`            | `1 - dot(a, b) / (norm(a) * norm(b))` |
|  Jaccard             |  `jaccard(a, b)`           | `1 - sum(min(a, b)) / sum(max(a, b))` |
|  Mahalanobis         |  `mahalanobis(a, b, vi)`   | `sqrt((a - b)' * vi * (a - b))` |
|  Manhattan           |  `manhattan(x, y)`         | `sum(abs(a - b))` |
|  Minkowski           |  `minkowski(x, y, p)`      | `sum(abs(a - b).^p) ^ (1/p)` |
