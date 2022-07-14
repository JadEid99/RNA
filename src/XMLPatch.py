## FUNCTION USED TO PATCH ##

def Patch(elemList, attList, seq_A):
    seq_A1 = list(seq_A)
    change = 0
    for i in range(len(elemList)):
        Command = elemList[i]
        if Command == "U":
            seq_A1[int(attList[i]['I']) + change - 1] = attList[i]['L']
        elif Command == "I":
            add = attList[i]['L']
            A_11 = seq_A1[0:int(attList[i]['I']) + change]
            A_12 = seq_A1[int(attList[i]['I']) + change:]
            seq_A1 = "".join(A_11) + add + "".join(A_12)
            change = change + 1
            seq_A1 = list(seq_A1)
        elif Command == "D":
            seq_A1[int(attList[i]['I']) + change - 1] = "±"

    return seq_A1