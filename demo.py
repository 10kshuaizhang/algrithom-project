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
import pyecharts
#from SmallestLastColor import SmallestLastColor
import time
from collections import defaultdict
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D




N = int(raw_input('N:'))
aveDegree =  int(raw_input("aveDegree:"))
unit = raw_input("Unit:")
g = nx.Graph()


'''
A still more efficient method is the cell method where 
the unit square is partitioned into a grid of 1 cells 
of size r*r and each vertex is put inthe appropriate 
cell as in bucket sort. The neighborsof each vertex 
are then determined by checking the distance of the 
vertex from all vertices of the nine cells
including and bounding the cell containing the vertex.
The expected number of pairwise distances checked is
then O(n2r2) generating the graph in O(n). Further-
more, the cell method is optimal in the sense of having
expected behavior per vertex of checking only a con-
stant times the average degree of each vertex, where
that constant is asymptotically 9 , as illustrated by the π
coverage ranges shown in Figure 3b. As illustrated in Figures 3a and 3b, 
the totality of edges may be found by checking vertex vi only against 
others in the shaded vertical strip for the lexicographic sweep 
line method or on the shaded pentonimo for the cell method as we me-
'''
start = time.time()
#data = []

if unit == "Sq":	
	r = math.sqrt(aveDegree/(N*math.pi))	
	cell = {}
	for i in range(int(1/r)+1):
		for j in range(int(1/r)+1):
			cell[(float(i),float(j))] = set()
	for _ in range(N):
		x = random.random()
		y = random.random()
		g.add_node((x,y))
		cell_n = (x//r,y//r)
		#cell = defaultdict(set)
		#cell = {}
		if cell_n in cell:
			cell[cell_n].add((x,y))
		else:
			cell[cell_n] = set((x,y))
		sourroundings = cell[(x//r,y//r)]
		if cell_n[0]-1>0 and cell_n[1]-1>0 and cell_n[0]+1<1/r and cell_n[1]+1<1/r:
			sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
		'''elif cell_n[0]-1<0 and cell_n[1]-1>0 and cell_n[0]+1<1/r and cell_n[1]+1<1/r:
									sourroundings|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
								elif cell_n[0]-1>0 and cell_n[1]-1<0 and cell_n[0]+1<1/r and cell_n[1]+1<1/r:
									sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]
								elif cell_n[0]-1>0 and cell_n[1]-1>0 and cell_n[0]+1<1/r and cell_n[1]+1>1/r:
									sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r,y//r-1)]
								elif cell_n[0]-1>0 and cell_n[1]-1>0 and cell_n[0]+1>1/r and cell_n[1]+1<1/r:
									sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]
		
						'''
		'''if N<=8000:
			for node in sourroundings:
				dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
				if dis<=r*r and dis>0:
					g.add_edge((x,y),(node[0],node[1]))
					#figure, ax = plt.subplots()
					line1 = [(x,y),(node[0],node[1])]
					(line1_xs, line1_ys) = zip(*line1)
					plt.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))

		else:
			for node in sourroundings:
				dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
				if dis<=r*r and dis>0:
					g.add_edge((x,y),(node[0],node[1]))

'''
	MAX = 0
	MIN = N
	SUM = 0
	for node in g.nodes():
		if g.degree(node) >= MAX:
			MAX = g.degree(node)
		elif g.degree(node) <= MIN:
			MIN = g.degree(node)
		SUM += g.degree(node)
	for node in g.nodes():
		if g.degree(node) == MAX:
			g.nodes[node]['color']= "yellow"
		if g.degree(node) == MIN:
			g.nodes[node]['color'] = "yellow"
	


	"""v1 = [node[0] for node in g.nodes()]
	v2 = [node[1] for node in g.nodes()]
	plt.scatter(v1,v2)"""
	#plt.plot()
	#plt.show() 
	'''v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.height = 800
		es.width = 800
		es.add("effectScatter", v1, v2,symbol_size = r*100)
		es.render()
	#colors = [n for n in range(N)]
	#print nx.algorithms.coloring.strategy_smallest_last(g,colors)
	#SmallestLastColor(g)

		v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.add("effectScatter", v1, v2)
		es.render()'''
elif unit == "Di":
	r = math.sqrt(aveDegree/N)
	cell = {}
	for i in range(int(1/r)+1):
		for j in range(int(1/r)+1):
			cell[(float(i),float(j))] = set()
	for _ in range(N):
		radius = random.random()
		angle = random.uniform(0,math.pi*2)
		if radius*math.cos(angle)>=0:
			x = math.sqrt(radius*math.cos(angle))
		else:
			x = 0-math.sqrt(radius*math.cos(angle))
		if radius*math.sin(angle)>=0:
			y = math.sqrt(-1*radius*math.sin(angle))
		else:
			y = 0-math.sqrt(-1*radius*math.sin(angle))
		g.add_node((x,y))
		cell_n = (x//r,y//r)
		if cell_n in cell:
			cell[cell_n].add((x,y))
		else:
			cell[cell_n] = set((x,y))
		sourroundings = cell[(x//r,y//r)]
		if cell_n[0]-1>0 and cell_n[1]-1>0 and cell_n[0]+1<1/r and cell_n[1]+1<1/r:
			sourroundings|cell[(x//r-1,y//r)]|cell[(x//r-1,y//r-1)]|cell[(x//r-1,y//r+1)]|cell[(x//r+1,y//r-1)]|cell[(x//r+1,y//r)]|cell[(x//r+1,y//r+1)]|cell[(x//r,y//r+1)]|cell[(x//r,y//r-1)]

		for node in sourroundings:
			dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)
			if dis<=r and dis>0:
				g.add_edge((x,y),node)
		v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.height = 800
		es.width = 800
		es.add("effectScatter", v1, v2)
		es.render()

elif unit == "Sp":# need revised because of radius is not right
	data = []
	r = math.sqrt(4*aveDegree/N)
	for n in range(N):
		theta = random.uniform(0,math.pi*2)
		phi = random.uniform(0,math.pi*2)
		x = math.sin(theta)*math.cos(phi)
		y = math.sin(theta)*math.sin(phi)
		z = math.cos(theta)
		data.append([x,y,z])
		g.add_node((x,y,z))
		for node in g.nodes():
			dis = (node[0]-x)*(node[0]-x)+(node[1]-y)*(node[1]-y)+(node[2]-z)*(node[2]-z)
			if dis<=r and dis>0:
				g.add_edge((x,y,z),node)
	S3 = pyecharts.Scatter3D("demo", width=1200, height=600)
	S3.add("",data,symbol_size = 1,is_visualmap=True)
	S3.render()
else:
	print "bad"
	exit()
end = time.time()
t = end - start
print "time:",t


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
for k in degreeList:
	print k,len(degreeList[k])
print "number_of_nodes:",g.number_of_nodes()
print "number_of_edges:",g.number_of_edges()
print "MAX:",MAX
print "MIN:",MIN
print "R:", r
print "AVE:",SUM/N

