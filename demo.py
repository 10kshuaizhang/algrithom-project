# usr/bin/env python 
# -*- coding:utf-8 -*- 
# Version : Python 2.7
# Editor : sublime text2
# Name : Zhang Shuai ID : 47499963

from __future__ import division
import networkx as nx
import random
import math
import time
from collections import defaultdict
import matplotlib.pyplot as plt 
from SmallestLastColor import SmallestLastColor
from SelectBackbone import selectBackbone
from RGGGeneratuion import RGGGeneration

from mpl_toolkits.mplot3d import Axes3D

N = int(raw_input('N:'))
aveDegree =  int(raw_input("aveDegree:"))
unit = raw_input("Unit:")
g = nx.Graph()

g,r,N,MAX,MIN, Dl = RGGGeneration(N,aveDegree,unit,g)
dll, dwd = SmallestLastColor(g)
top2, indeSet = selectBackbone(g,r)

# draw RGG 
drawRGG = raw_input("drawRGG?-->")
if drawRGG == 'Y':
    
    plt.axis("equal")
    ax = plt.gca()
    ax.set_aspect(1)

    d = [k for k in Dl]
    v = [len(Dl[k]) for k in Dl]
    plt.bar(d,v)
    plt.axis('auto')
    plt.title("degree list")
    plt.show()
    if N<=8000:
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
    
    max_node = []
    min_node = []
    for node in g.nodes():
        if g.degree(node) == MAX:
            max_node.append(node)
        if g.degree(node) == MIN:
            min_node.append(node)
    max1 = [node[0] for node in max_node]
    max2 = [node[1] for node in max_node]
    plt.scatter(max1,max2,color= 'green',linewidths= 3)
    min1 = [node[0] for node in min_node]
    min2 = [node[1] for node in min_node]
    plt.scatter(min1,min2,color= 'yellow',linewidths= 3)
    
    plt.show()
else:
    pass


drawdwd = raw_input("drawdwd?-->")
if drawdwd == 'Y':
    tmpdll = reversed(dll)
    y1 = [g.degree(node) for node in tmpdll]
    y2 = dwd
    x = range(1,len(dll)+1)
    plt.plot(x,y1,c = 'red',linewidth = 1,label = 'upper bound')
    plt.plot(x,y2,c = 'blue',linewidth = 1,label = 'degree-when-deleted')
    plt.axis("auto")
    plt.title("sequential color Plot")
    plt.legend()
    plt.show()

    d = [k for k in indeSet]
    v = [len(indeSet[k]) for k in indeSet]
    plt.bar(d,v)
    plt.axis('auto')
    plt.title("color distribution")
    plt.show()

drawback = raw_input("draw backbone?-->")
if drawback == 'Y':
#draw backbone 1
    plt.axis("equal")
    ax = plt.gca()
    ax.set_aspect(1)
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for edge in top2[0].edges():
        x1.append(edge[0][0])
        y1.append(edge[0][1])
        x2.append(edge[1][0])
        y2.append(edge[1][1])
    plt.plot([x1,x2],[y1,y2],linewidth=0.5,color='blue',alpha =0.5)

    vx = [node[0] for node in top2[0]]
    vy = [node[1] for node in top2[0]]
    plt.scatter(vx,vy,color = "red",linewidth=0.2)
    plt.show()

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for edge in top2[1].edges():
        x1.append(edge[0][0])
        y1.append(edge[0][1])
        x2.append(edge[1][0])
        y2.append(edge[1][1])
    plt.plot([x1,x2],[y1,y2],linewidth=0.5,color='blue',alpha =0.5)

    vx = [node[0] for node in top2[1]]
    vy = [node[1] for node in top2[1]]
    plt.scatter(vx,vy,color = "yellow",linewidth=0.2)
    plt.axis("equal")
    plt.show() 
else:
    exit()
