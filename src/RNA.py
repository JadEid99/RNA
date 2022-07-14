from xmlrpc.client import DateTime

from EditDistance import find_distance
from XMLPatch import Patch
from BackTracking import BackTrack, BackTrackFULL
from XMLWrite import XMLWrite
from XMLRead import parser
from GetRNA import GetRNA
from xml.etree.ElementTree import ElementTree
from datetime import datetime

s1 = 1
s2 = 9
RNA = GetRNA(s1, s2)

# mydoc = ElementTree(file='Database.xml')
# for e in mydoc.findall('/S727462'):
#     print(e.text)


# A = RNA[0]
# B = RNA[1]
A = ["13213", "Human", "GAG", 3]
B = ["13113", "Human", "AGA", 3]

seq_A = A[2]
seq_B = B[2]

print(seq_A)
print(seq_B)

Diff = find_distance(A, B)
EditScript = BackTrackFULL(Diff, A, B)

XMLWrite(EditScript, A, B)

elemList, attList = parser("EditScript.xml")

seq_A1 = Patch(elemList, attList, seq_A)

print("Distance = " + str(Diff[A[3], B[3]]))
print("------------------------------------------------------")
print("".join(seq_A1).replace("±", ""))
print(seq_B)
