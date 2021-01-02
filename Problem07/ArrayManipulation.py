import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*n
    for query in queries:
        a[query[0] - 1] += query[2]
        if query[1] != len(a):
            a[query[1]] -= query[2]
    max1 = 0
    b = 0
    for q in a:
        b += q
        if b > max1:
            max1 = b
    return max1 

n = 10
queries=[[1,5,3],[4,8,7],[6,9,1]]
result = arrayManipulation(n, queries)
