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
from SmallestLastColor import SmallestLastColor
import time
from collections import defaultdict



N = int(raw_input('N:'))
aveDegree =  int(raw_input("aveDegree:"))
unit = raw_input("Unit:")
g = nx.Graph()



start = time.time()
#data = []

if unit == "Sq":	
	r = math.sqrt(aveDegree/(N*math.pi))	
	for _ in range(N):
		x = random.random()
		y = random.random()
		g.add_node((x,y))
		for node in g.nodes():
			dis = abs(node[0]*node[0] - x*x)+abs(node[1]*node[1] - y*y)
			if dis<=r*r and dis>0:
				g.add_edge((x,y),node)
		'''v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.height = 800
		es.width = 800
		es.add("effectScatter", v1, v2,symbol_size = 5)
		es.render()'''
	#colors = [n for n in range(N)]
	#print nx.algorithms.coloring.strategy_smallest_last(g,colors)
	#SmallestLastColor(g)

		'''v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.add("effectScatter", v1, v2)
		es.render()'''
elif unit == "Di":
	r = math.sqrt(aveDegree/N)
	for n in range(N):
		radius = random.random()
		angle = random.uniform(0,math.pi*2)
		x = radius*math.cos(angle)
		y = radius*math.sin(angle)
		g.add_node((x,y))
		for node in g.nodes():
			dis = math.sqrt(abs(node[0]*node[0] - x*x)+abs(node[1]*node[1] - y*y))
			if dis<=r and dis>0:
				g.add_edge((x,y),node)
		v1 = [node[0] for node in g.nodes()]
		v2 = [node[1] for node in g.nodes()]
		es = pyecharts.Scatter("demo")
		es.height = 800
		es.width = 800
		es.add("effectScatter", v1, v2,symbol_size = 5)
		es.render()

elif unit == "Sp":# need revised because of radius is not right
	data = []
	r = math.sqrt(aveDegree/N)
	for n in range(N):
		theta = random.uniform(0,math.pi*2)
		phi = random.uniform(0,math.pi*2)
		x = math.sin(theta)*math.cos(phi)
		y = math.sin(theta)*math.sin(phi)
		z = math.cos(theta)
		data.append([x,y,z])
		g.add_node((x,y,z))
		for node in g.nodes():
			dis = math.sqrt(abs(node[0]*node[0] - x*x)+abs(node[1]*node[1] - y*y)+abs(node[2]*node[2] - z*z))
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

