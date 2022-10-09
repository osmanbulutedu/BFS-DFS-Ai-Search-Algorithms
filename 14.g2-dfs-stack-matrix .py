# P1-14: Graph2 DFS-Stack by using MATRIX.  (Osman Bulut-001530539)
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

# I'll keep track visited set, and also total traversal and the path until finding the goal node
visited = []
path = [6] #goal node is in the return path as given state.6 is matrix index representation of 'G'
parents = {11: 'None'} #source node dont have a parent


# I'll define my dfs function with using only stack.
# I'll get the visited list, vertice list information and the source node information to initialize the search.
def dfs(graph, source, goal):  # function for dfs
    stack=[source]
    while stack and goal not in visited:  # instead of recursion I'll use a single while loop until hitting the goal node.
        expanded = stack.pop()
        if expanded not in visited:
            visited.append(expanded)
        for i in reversed(list(range(len(graph)))):
            if graph[expanded][i] == 1:
                if not i in visited:
                    stack.append(i)
                    parents[i] = expanded  # I'll save all expanded nodes' children



    # now we can follow track the parents starting from the goal
    if goal in parents:
        i = goal
        while not path[-1] == source:
            path.append(parents[i])
            i = path[-1]


dfs(g2matrix, 11,6)  #graph, source and goal node are my inputs. 6 is node 'G' and 11 is node 's' in terms of the matrix.

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


