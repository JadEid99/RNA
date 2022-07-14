import sys

from XMLPatch import Patch
from XMLRead import parser

seq_A = sys.argv[1]
Loadpath = sys.argv[2]
savepath = sys.argv[3]

# seq_A = "AG"
# Loadpath = "D:/UnityProjects/RNASeq/Assets/diff1.xml"

elemList, attList = parser(Loadpath)

seq_A1 = Patch(elemList, attList, seq_A)

dataFile = open(savepath + "/Patcheddata.txt", "w")
dataFile.write("".join(seq_A1).replace("±", ""))
dataFile.close()

print(0)
