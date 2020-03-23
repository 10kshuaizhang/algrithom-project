'''
5 after coloring all nodes
theoritically , combine two independent sets will be bipartite
6 need to do:
a.pick first 4 color sets of largest order(number of nodes in graph theory topology) 
b.and randomly pair any 2 of them(get 6 pairs)
c.delete the minor componets
d.and pick 2 largest size(number of edges)
e.then delete the tail(delete the node of degree one)
'''
from __future__ import division
from collections import defaultdict
import random
import networkx as nx
import matplotlib.pyplot as plt 
import time

def selectBackbone(graph, r):
    selectStart = time.time()


    indeSet = defaultdict(list)
    for node in graph.nodes():
        indeSet[graph.nodes[node]['color']].append(node)
    indeSet_copy = indeSet.copy()
    
    #pick first 4 color sets of largest order(number of nodes in graph theory topology) 
    
    top4 = []
    for _ in range(4):
        MAX = 0
        for k in indeSet:
            if len(indeSet[k])>=MAX:
                MAX = len(indeSet[k])
                largest = k
        top4.append(indeSet[largest])
        del indeSet[largest]


    tmpg = graph.subgraph(top4[0]+top4[1]).copy()
    subgraphs = [tmpg]
    tmpg = graph.subgraph(top4[0]+top4[2]).copy()
    subgraphs.append(tmpg)
    tmpg = graph.subgraph(top4[0]+top4[3]).copy()
    subgraphs.append(tmpg)
    tmpg = graph.subgraph(top4[1]+top4[2]).copy()
    subgraphs.append(tmpg)
    tmpg = graph.subgraph(top4[3]+top4[2]).copy()
    subgraphs.append(tmpg)
    tmpg = graph.subgraph(top4[1]+top4[3]).copy()
    subgraphs.append(tmpg)

    #delete the minor componets
    for n in range(len(subgraphs)):
        tmp = [node for node in subgraphs[n].nodes()]
        for node in tmp:
            if subgraphs[n].degree[node] == 0:
                subgraphs[n].remove_node(node)
        
    #pick 2 largest size(# of edge)
    top2 = []
    for _ in range(2):
        MAX = 0
        largest = subgraphs[0]
        for subgraph in subgraphs:
            if subgraph.size()>MAX:
                MAX = subgraph.size()
                largest = subgraph
        top2.append(largest)
        subgraphs.remove(largest)

   #then delete the tail(delete the node of degree one)
    for i in range(2):
        tmp2 = [node for node in top2[i].nodes()]
        for node in tmp2:
            if top2[i].degree[node] == 1 and top2[i].degree[node] == 0:
                top2[i].remove_node(node)

    #coverage
    for i in range(2):
        c = []
        n = 0
        for _ in range(1000):
            c.append((random.random(),random.random()))

        for cc in c[:]:
            for node in top2[i].nodes():
                if (cc[0]-node[0])**2+(cc[1]-node[1])**2 <r*r:
                    n += 1
                    break
    
        print "top",i+1, "has ", top2[i].number_of_nodes(),"nodes", top2[i].number_of_edges(),"edges and coverage is ",i,":", n/1000
    selectEnd = time.time()
    print "selectBackbone time: ", selectEnd - selectStart
    print len(top2[0])
    print len(top2[1])
    return top2,indeSet_copy

