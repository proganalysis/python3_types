# your code goes here
# your code goes here
# your code goes here
#!/bin/python3

import sys
def getKey(x):
    return x[0]
def twinArrays(ar1, ar2):
    # Complete this function
    ar3=[[0 for i in range(2)] for j in range(len(ar1))]
    ar4=[[0 for i in range(2)] for j in range(len(ar2))]
    for i in range(len(ar1)):
        ar3[i][0]=ar1[i]
        ar3[i][1]=i
        ar4[i][0]=ar2[i]
        ar4[i][1]=i
    ar3.sort(key = getKey)
    ar4.sort(key = getKey)
    i=0
    if (ar3[i][1]==ar4[i][1]):
        if (ar3[i+1][0]-ar3[i][0])<(ar4[i+1][0]-ar4[i][0]):
            return ar3[i+1][0]+ar4[i][0]
        else :
            return ar3[i][0]+ar4[i+1][0]
    return ar3[0][0]+ar4[0][0]
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
