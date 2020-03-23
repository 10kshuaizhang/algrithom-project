from __future__ import division
import networkx as nx
import random
import math
import time
from collections import defaultdict
import matplotlib.pyplot as plt 

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
N = int(raw_input('N:'))
aveDegree =  int(raw_input("aveDegree:"))
g = nx.Graph()
r = math.sqrt(aveDegree/(N*math.pi))
start = time.time()
r = math.sqrt(aveDegree/N)
cell = defaultdict(set)
for i in range(int(1/r)+1):
    for j in range(int(1/r)+1):
        cell[(float(i),float(j))] = set()
for _ in range(N):
    radius = random.random()
    angle = random.uniform(0,math.pi*2)
    x = math.sqrt(radius)*math.cos(angle)+1
    y = math.sqrt(radius)*math.sin(angle)+1
    g.add_node((x,y))

    cell_n = (x//r,y//r)
    cell[cell_n].add((x,y))
    sourroundings = cell[(x//r,y//r)]
    if cell_n[0]-1>=0 and cell_n[0]+1<=2/r:
        if cell_n[1]-1>=0 and cell_n[1]+1<=2/r:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
        elif cell_n[1]-1<=0:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]
        elif cell_n[1]+1>2/r:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r,y//r-1)]
    elif cell_n[0]-1<0:
        if cell_n[1]-1>=0 and cell_n[1]+1<=2/r:
            sourroundings = sourroundings|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
        elif cell_n[1]-1<0:
            sourroundings = sourroundings|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]
        elif cell_n[1]+1>2/r:
            sourroundings = sourroundings|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r,y//r-1)]
    elif cell_n[0]+1>2/r:
        if cell_n[1]-1>=0 and cell_n[1]+1<=2/r:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
        elif cell_n[1]-1<0:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r+1)]|cell[(x//r,y//r+1)]
        elif cell_n[1]+1>2/r:
            sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r+1,y//r-1)]|cell[(x//r,y//r-1)]
    for node in g.node():
    #for node in sourroundings:
        dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
        if dis<=r*r and dis>0:
            g.add_edge((x,y),(node[0],node[1]))
end = time.time()
print "time:" , end-start

x1 = []
y1 = []
x2 = []
y2 = []
for edge in g.edges():
    x1.append(edge[0][0])
    y1.append(edge[0][1])
    x2.append(edge[1][0])
    y2.append(edge[1][1])

plt.plot([x1,x2],[y1,y2],linewidth=0.5,color='blue',alpha =0.4)

plt.axis("equal")
ax = plt.gca()
ax.set_aspect(1)
v1 = [node[0] for node in g.nodes()]
v2 = [node[1] for node in g.nodes()]
plt.scatter(v1,v2,color= 'red',linewidths= 1,alpha =0.7)
plt.show()