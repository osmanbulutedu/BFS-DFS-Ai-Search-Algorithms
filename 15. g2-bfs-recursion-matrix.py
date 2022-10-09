# P1-15: Graph2 BFS-Recursion by using MATRIX.  (Osman Bulut-001530539)


import numpy as np

g2matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]])

visited = []
parents = {11: 'None'}
goal = 6
path = [goal]


def bfs(graph, source, visited):  # I'll get graph, source node and visited list as input
    if not source:
        return []  # when I get empty list, recursions will end.
    else:
        expanded = source.pop(0)

        visited.append(expanded)

        for i in range(len(graph)):  # I have 12 nodes for this example.I'll need to search them all to find children.
            if graph[expanded][i] == 1:
                if i not in visited and i not in source:
                    source.append(i)
                    parents[i] = expanded  #I'm tracking the parents of my nodes.

        if goal in parents:  # now we can also create our return path if we had hid the goal node.
            l = goal
            while not path[-1] == 11:
                path.append(parents[l])
                l = path[-1]

        bfs(graph, source, visited)  # RECURSION LINE


bfs(g2matrix, [11], visited)  # the 11 is my source node. 11 represents 's' node in my matrix. If I implement maps[11], it returns 's'.

#I'm not sure about what format is wanted in the homework. Therefore I'll give both as numbers and characters)
print('The return path is as matrix index numbers ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is as matrix index numbers ---->", visited)


# I'll need a map between numbers and characters.
maps = ['a','b','c','d','e','f','G','h','p','q','r','s']
pathchc=[]
visitedchc=[]
for i in list(reversed(path)):
    pathchc.append(maps[i])
for i in visited:
    visitedchc.append(maps[i])

print('The return path is as characters ----> ', pathchc)
print("The expanded vertex list until reaching the destination is as characters ---->", visitedchc)






