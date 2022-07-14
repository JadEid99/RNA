import numpy as np
from NucleotideDictionary import *


## FUNCTION USED TO FIND DISTANCE ##
def find_distance(A, B):
    seq_A = A[2]
    seq_B = B[2]
    Diff = np.zeros((A[3] + 1, B[3] + 1))

    ## First column and first row ##
    Diff[:, 0] = range(A[3] + 1)
    Diff[0, :] = range(B[3] + 1)

    ## Filling up distance matrix ##
    for i in range(1, A[3] + 1):
        for j in range(1, B[3] + 1):
            x = seq_A[i - 1]
            y = seq_B[j - 1]
            Diff[i, j] = min(Diff[i - 1, j] + 1,
                             Diff[i, j - 1] + 1,
                             Diff[i - 1, j - 1] + getUpdateCost(x, y))
    return Diff


def getUpdateCost(a, b):
    return catalog[a].getCost(catalog[b].listChar)
