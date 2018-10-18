


#TODO:
'''
1 how to generate bipartite subgraph?
(independents sets?)
2 how to generate 2 independent sets? 
3 vetex coloring-> labeling 
in current project, we use sequential coloring algorithm


sequential-> ordering 
so smallest coloring ordering ->(first way)
smallest degree out of graph 
into a container like stack
then traversal all the nodes in order
note that every time you pop a node, ajacent nodes degree reduce 1
find neighbors(remember deleted node are no longer neighbor)
degree when deleted
then color from the first(top in stack)
    when coloring, check the neighbors
one color one dependent set

4 how make smallest last ordering efficient(second liniear time way)
esatblish degree list
    after pop, modify the list, its ajacent node(looking into ajacency list) 'degrade 1'
    double link list to esatblish degree list
    when use lib, it will iterate the list, but manually 
    say right in left out ,first one and last one
    hash table may be used in degree list




5 after coloring all nodes
theoritically , combine two independent sets will be bipartite
6 need to do:
a.pick first 4 color sets of largest order(number of nodes in graph theory topology) 
b.and randomly pair any 2 of them(get 6 pairs->5 bipartite subgraph) 
c.delete the minor componets
d.and pick 2 largest size(number of edges)
e.then delete the tail(delete the node of degree one)

'''



#TODO
#1 traversal all the nodes and push in a degree list(doubly link list)but in python,
#actually a list is not really linear time when operate it -> so use hash table to make it linear in theory
#2 from the smallest degree put into individual data sturcture (USING ajacency list) 
#.  at the same time, when delete one nodes, 
#.  its ajacent nodes shoudl mines one degree
#
#greedy color:each time try to give a small color
from collections import defaultdict, deque
import networkx as nx
import random
import math
import itertools
import matplotlib.pyplot as plt 
import time

def SmallestLastColor(graph):
    colorStart = time.time()
    MIN = float('inf')
    gg = graph.copy()
    degreeList = defaultdict(set)#set is faster than list in some way
    dll = deque()
    for node,d in gg.degree:
        degreeList[d].add(node)
        MIN = min(d,MIN)

    def MinDeg():
        return next(n for n in itertools.count(MIN) if n in degreeList)
    dwd = deque()
    #cliquesize = deque()
    for i in graph:
        '''noden = gg.number_of_nodes()
                                edgen = gg.number_of_edges()
                                if  edgen == noden*(noden-1)/2:
                                    cliquesize.append(noden)'''
            #walkthrough
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for edge in gg.edges():
            x1.append(edge[0][0])
            y1.append(edge[0][1])
            x2.append(edge[1][0])
            y2.append(edge[1][1])
        plt.plot([x1,x2],[y1,y2],linewidth=0.5,color='blue',alpha =0.5)

        vx = [node[0] for node in gg]
        vy = [node[1] for node in gg]
        plt.scatter(vx,vy,color = "red",linewidth=0.5)
        plt.axis("equal")
        plt.title("walkthrough")
        plt.show()
        #print "terminal clique size: ", cliquesize[0]

        minDeg = MinDeg()
        tmp = degreeList[minDeg].pop()
        if not degreeList[minDeg]:
            del degreeList[minDeg]

        dll.appendleft(tmp)
        
        #dwd.append(gg.degree(tmp))

        for v in gg[tmp]:
            degree = gg.degree(v)
            degreeList[degree].remove(v)
            if not degreeList[degree]:  
                del degreeList[degree]
            degreeList[degree - 1].add(v)
        gg.remove_node(tmp)     
        MIN = minDeg - 1


    for node in dll:
        if 'color'  not in graph.nodes[node]:
            graph.nodes[node]['color'] = 1
        tmp = []
        for neighbor in graph.adj[node]:
            if 'color' in graph.nodes[neighbor]:
                tmp.append(graph.nodes[neighbor]['color'])
        for neighbor in graph.adj[node]:
            if 'color' in graph.nodes[neighbor] and graph.nodes[neighbor]['color']==graph.nodes[node]['color']:
                while True:
                    graph.nodes[node]['color'] += 1
                    if graph.nodes[node]['color'] not in tmp:
                        break
    colorEnd = time.time()

    '''indeSet = defaultdict(list)
                colorsize = deque()
                for node in graph.nodes():
                    indeSet[graph.nodes[node]['color']].append(node)
                for k in indeSet:
                    colorsize.append(len(indeSet[k]))
                    '''
    
    '''print " max degree-when-deleted : ",max(dwd)
                print "# of colors ", len(indeSet)
                print "max color size: ", max(colorsize)
                print "terminal clique size: ", max(cliquesize)'''
    print "colrotime: ", colorEnd - colorStart 
    return dll, dwd
    



