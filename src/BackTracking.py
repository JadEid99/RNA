## FUNCTION USED TO FIND EDIT SCRIPT ##
from Operations import *


def BackTrack(Diff, A, B):
    i = A[3]
    j = B[3]
    EditScript = []
    ESOperations = []
    while i > 0 or j > 0:
        ## If last edit is not update, this decides if it is insert or delete ##
        if i == 0 and j != 1:
            EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
            ESOperations.append(Insert(i, B[2][j-1]))
            j = j - 1
        elif i != 1 and j == 0:
            EditScript.append("Delete A[" + str(i + 1) + "]")
            ESOperations.append(Delete(i))
            i = i - 1
        else:
            ## Update has the minimum distance ##
            if min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j - 1] and A[2][i - 1] == B[2][j - 1]:
                i = i - 1
                j = j - 1
            ## Update with the same characters has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j - 1] and A[2][i - 1] != B[2][j - 1]:
                EditScript.append("Update A[" + str(i) + "] with B[" + str(j) + "]")
                ESOperations.append(Update(i, B[2][j-1]))
                i = i - 1
                j = j - 1
            ## Delete has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j]:
                EditScript.append("Delete A[" + str(i) + "]")
                ESOperations.append(Delete(i))
                i = i - 1
            ## Insert has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i, j - 1]:
                EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
                ESOperations.append(Insert(i, B[2][j-1]))
                j = j - 1

    if i == 1 and j != 1:
        EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
        ESOperations.append(Insert(i, B[2][j-1]))

    if i != 1 and j == 1:
        EditScript.append("Delete A[" + str(1) + "]")
        ESOperations.append(Delete(0))


    start = 0
    end = len(EditScript)-1
    while start < end:
        EditScript[start], EditScript[end] = EditScript[end], EditScript[start]
        start += 1
        end -= 1

    start = 0
    end = len(ESOperations)-1
    while start < end:
        ESOperations[start], ESOperations[end] = ESOperations[end], ESOperations[start]
        start += 1
        end -= 1

    return ESOperations





def BackTrackFULL(Diff, A, B):
    i = A[3]
    j = B[3]
    EditScript = []
    ESOperations = []
    while i > 0 or j > 0:
        ## If last edit is not update, this decides if it is insert or delete ##
        if i == 0 and j != 1:
            EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
            ESOperations.append(Insert(i, B[2][j-1]))
            j = j - 1
        elif i != 1 and j == 0:
            EditScript.append("Delete A[" + str(i + 1) + "]")
            ESOperations.append(Delete(i))
            i = i - 1
        else:
            ## Update has the minimum distance ##
            if min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j - 1] and A[2][i - 1] == B[2][j - 1]:
                i = i - 1
                j = j - 1
                ESOperations.append(FakeUpdate(i, B[2][j-1]))
            ## Update with the same characters has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j - 1] and A[2][i - 1] != B[2][j - 1]:
                EditScript.append("Update A[" + str(i) + "] with B[" + str(j) + "]")
                ESOperations.append(Update(i, B[2][j-1]))
                i = i - 1
                j = j - 1
            ## Delete has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i - 1, j]:
                EditScript.append("Delete A[" + str(i) + "]")
                ESOperations.append(Delete(i))
                i = i - 1
            ## Insert has the minimum distance ##
            elif min(Diff[i, j - 1], Diff[i - 1, j], Diff[i - 1, j - 1]) == Diff[i, j - 1]:
                EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
                ESOperations.append(Insert(i, B[2][j-1]))
                j = j - 1

    if i == 1 and j != 1:
        EditScript.append("Insert B[" + str(j) + "] in A[" + str(i) + "]")
        ESOperations.append(Insert(i, B[2][j-1]))

    if i != 1 and j == 1:
        EditScript.append("Delete A[" + str(1) + "]")
        ESOperations.append(Delete(0))


    start = 0
    end = len(EditScript)-1
    while start < end:
        EditScript[start], EditScript[end] = EditScript[end], EditScript[start]
        start += 1
        end -= 1

    start = 0
    end = len(ESOperations)-1
    while start < end:
        ESOperations[start], ESOperations[end] = ESOperations[end], ESOperations[start]
        start += 1
        end -= 1

    return ESOperations


