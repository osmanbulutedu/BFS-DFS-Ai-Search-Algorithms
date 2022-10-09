# P1-8: Graph1 BFS-Stack by using MATRIX.  (Osman Bulut-001530539)
import numpy as np

g1matrix=np.array([[0,1,1,0,0,0,0,0,0,0,0,0],
         [1,0,0,1,0,0,0,0,0,0,0,0],
         [1,0,0,1,0,1,0,0,0,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,1],
         [0,0,0,1,0,0,0,1,0,0,1,1],
         [0,0,1,0,0,0,1,0,0,0,1,0],
         [0,0,0,0,0,1,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,1,1,0,0],
         [0,0,0,0,0,0,0,1,0,1,0,1],
         [0,0,0,0,0,0,0,1,1,0,0,0],
         [0,0,0,0,1,1,0,0,0,0,0,0],
         [0,0,0,1,1,0,0,0,1,0,0,0]])

def bfs(graph, source, goal):  # my function's input will be graph data, source node, and goal node.
    # initial parameters
    stack=[source]
    visited = []
    path = [goal]
    parents = {11: 'None'}

    # Now, I'll create a loop. I'll iterate this loop as long as there is an item in the stack and not arriving the goal node.

    while not stack == [] and goal not in visited:
        expanded = stack.pop(0)

        visited.append(expanded)


        for i in range(len(graph)):  # I have 12 nodes for this example.I'll need to search them all to find children.
            if graph[expanded][i]==1:
                if i not in visited and i not in stack:
                    stack.append(i)
                    parents[i] = expanded  #I'm tracking the parents of my nodes.

    if goal in parents:  # now we can also create our return path if we had hid the goal node.
        l = goal
        while not path[-1] == source:
            path.append(parents[l])
            l = path[-1]

    return (visited, list(reversed(path)))


visited, path = bfs(g1matrix, 11, 6)  # I put graph data, source node info and goal node info into my function


#I'm not sure about what format is wanted in the homework. Therefore, I'll give both as matrix index numbers and characters)
print('BFS Expanded Vertices until finding the goal node is as matrix index numbers---->', visited)
print('Return path is as matrix index numbers ----> ', path)

# I'll need a map between numbers and characters.
maps = ['a','b','c','d','e','f','G','h','p','q','r','s']
pathchc=[]
visitedchc=[]
for i in path:
    pathchc.append(maps[i])
for i in visited:
    visitedchc.append(maps[i])

print('The return path is as characters ----> ', pathchc)
print("The expanded vertex list until reaching the destination is as characters ---->", visitedchc)

