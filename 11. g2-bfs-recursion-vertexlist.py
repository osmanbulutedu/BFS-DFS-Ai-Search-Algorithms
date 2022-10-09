# P1-11: Graph2 BFS-Recursion by using VERTEX LIST.  (Osman Bulut-001530539)


import numpy as np
g2={
    'a':[],
    'b':['a'],
    'c':['a'],
    'd':['b','c','e'],
    'e':['h','r'],
    'f':['c','G'],
    'G':[],
    'h':['p','q'],
    's':['d','e','p'],
    'p':['q'],
    'q':[],
    'r':['f']
}

#my initial parameters must be outside of the function. Bcs we will use recursion.
visited=[]
parents={'s':'None'}
goal='G'
path=[goal]
def bfs(graph,source,visited):
    if not source: #recursion break rule
        return []
    else:
        expanded=source.pop(0)

        visited.append(expanded)

        for i in graph[expanded]:   #in the loop I'll encode the parents of the nodes while I'm determining neighbors
                if i not in visited and i not in source:
                    source.append(i)
                    parents[i] = expanded

        if goal in parents:  #now we can also create our return path if we had hid the goal node.
            i = goal
            while not path[-1] == 's':
                path.append(parents[i])
                i = path[-1]

        bfs(graph,source,visited) #RECURSION LINE

bfs(g2,['s'],visited)  #graph data, source node as list, and visited initial parameter are my inputs
print('The return path is ----> ',list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)

