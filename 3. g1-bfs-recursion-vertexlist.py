# P1-3: Graph1 BFS-Recursion by using VERTEX LIST.  (Osman Bulut-001530539)


import numpy as np

g1 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'c', 'e', 's'],
    'e': ['d', 'h', 'r', 's'],
    'f': ['c', 'G', 'r'],
    'G': ['f'],
    'h': ['e', 'p', 'q'],
    'p': ['h', 'q', 's'],
    'q': ['h', 'p'],
    'r': ['e', 'f'],
    's': ['d', 'e', 'p']}

#my initial parameters must be outside of the function. Bcs we will use recursion.
visited = []
parents = {'s': 'None'}
goal = 'G'
path = [goal]


def bfs(graph, source, visited):
    if not source:      #recursion break rule
        return []
    else:
        expanded = source.pop(0)

        visited.append(expanded)

        for i in graph[expanded]:       #in the loop I'll encode the parents of the nodes while I'm determining neighbors
            if i not in visited and i not in source:
                source.append(i)
                parents[i] = expanded

        if goal in parents: #now we can also create our return path if we had hid the goal node.
            i = goal
            while not path[-1] == 's':
                path.append(parents[i])
                i = path[-1]

        bfs(graph, source, visited) #RECURSION LINE


bfs(g1, ['s'], visited)  #graph data, source node as list, and visited initial parameter are my inputs
print('The return path is ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)

