from __future__ import division
import networkx as nx
import random
import math
import time
from collections import defaultdict
import matplotlib.pyplot as plt 
from SmallestLastColor import SmallestLastColor
from SelectBackbone import selectBackbone
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def RGGGeneration(N,aveDegree,unit,g):
    RGGstart = time.time()

    if unit == "Sq":    
        r = math.sqrt(aveDegree/(N*math.pi))
        cell = defaultdict(set)
        for i in range(int(1/r)+1):
            for j in range(int(1/r)+1):
                cell[(i,j)] = set()
        for _ in range(N):
            x = random.random()
            y = random.random()
            g.add_node((x,y))
            cell_n = (x//r,y//r)
            cell[cell_n].add((x,y))
            sourroundings = cell[(x//r,y//r)]

            if cell_n[0]-1>=0 and cell_n[0]+1<=1/r:
                if cell_n[1]-1>=0 and cell_n[1]+1<=1/r:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
                elif cell_n[1]-1<0:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]
                elif cell_n[1]+1>1/r:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r,y//r-1)]
            elif cell_n[0]-1<0:
                if cell_n[1]-1>=0 and cell_n[1]+1<=1/r:
                    sourroundings = sourroundings|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
                elif cell_n[1]-1<0:
                    sourroundings = sourroundings|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]
                elif cell_n[1]+1>1/r:
                    sourroundings = sourroundings|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r,y//r-1)]
            elif cell_n[0]+1>1/r:
                if cell_n[1]-1>=0 and cell_n[1]+1<=1/r:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
                elif cell_n[1]-1<0:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r+1)]|cell[(x//r,y//r+1)]
                elif cell_n[1]+1>1/r:
                    sourroundings = sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r+1,y//r-1)]|cell[(x//r,y//r-1)]
            #for node in g.node():
            for node in sourroundings:
                dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
                if dis<=r*r and dis>0:
                    g.add_edge((x,y),(node[0],node[1]))

    elif unit == "Di":
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
            #for node in g.node():
            for node in sourroundings:
                dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
                if dis<=r*r and dis>0:
                    g.add_edge((x,y),(node[0],node[1]))


    elif unit == "Sp":# need revised because of radius is not right
        r = math.sqrt(4*aveDegree/N)
        for n in range(N):
            theta = random.uniform(0,math.pi*2)
            phi = random.uniform(0,math.pi*2)
            x = math.sin(theta)*math.cos(phi)
            y = math.sin(theta)*math.sin(phi)
            z = math.cos(theta)
            g.add_node((x,y,z))
            for node in g.nodes():
                dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)+(node[2]-z)*(node[2]-z)
                if dis<=r and dis>0:
                    g.add_edge((x,y,z),node)
        v1 = [node[0] for node in g.nodes()]
        v2 = [node[1] for node in g.nodes()]
        v3 = [node[2] for node in g.nodes()]

        for node in g.node():
            dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)+(node[2]-z)*(node[2]-z)
            if dis<=r*r and dis>0:
                g.add_edge((x,y,z),(node[0],node[1]),node[2])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(v1,v2,v3,color= 'red',linewidths= 3,alpha =0.7)
        plt.show()

    else:
        print("bad")
        exit()
    RGGend = time.time()

      
    MAX = 0
    MIN = N
    SUM = 0
    for node in g.nodes():
        if g.degree(node) >= MAX:
            MAX = g.degree(node)
        elif g.degree(node) <= MIN:
            MIN = g.degree(node)
        SUM += g.degree(node)
    degreeList = defaultdict(set)#set is faster than list in some way
    for node,d in g.degree:
        degreeList[d].add(node)

    print("number_of_nodes:",g.number_of_nodes())
    print ("number_of_edges:",g.number_of_edges())
    print( "MAX:",MAX)
    print( "MIN:",MIN)
    print("R:", r)
    print("AVE:",SUM/N)
    print "generation time:",RGGend - RGGstart 
    return g,r,N,MAX,MIN,degreeList