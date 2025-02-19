#!/usr/bin/python3
import sys
import string
import math
classes=[[5.8,4.0,'Iris-setosa'],[6.1,2.8,'Iris-versicolor'],[6.3,2.7,'Iris-virginica']]
linecount=1
for line in sys.stdin:
    line=line.strip()
    features=line.split(',')
    min = [10000,-1]
    for i in range(0,len(classes)):
        dist=math.dist([float(features[0]),float(features[1])],[classes[i][0],classes[i][1]])
        if(dist< min[0]):
            min[0] = dist
            min[1] = i
    print(f'{min[1]},{linecount},1,{float(features[0])},{float(features[1])}')
    linecount = linecount+1
