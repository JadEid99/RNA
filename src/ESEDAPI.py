import os
import sys
import json
from BackTracking import BackTrackFULL
from EditDistance import find_distance
from XMLWrite import EStoString

s1 = sys.argv[1]
s2 = sys.argv[2]
path = sys.argv[3]

# s1 = "GAG"
# s2 = "GGA"

A = ["13213", "Human", s1, len(s1)]
B = ["13113", "Human", s2, len(s2)]

Diff = find_distance(A, B)
# EditScript = BackTrack(Diff, A, B)
EditScript = BackTrackFULL(Diff, A, B)

data = {}
data['Matrix'] = json.dumps(Diff.tolist())
data['ES'] = EStoString(EditScript, A, B)

dataFile = open(path + "/ESdata.txt", "w")
dataFile.write(json.dumps(data))
dataFile.close()

print(0)
