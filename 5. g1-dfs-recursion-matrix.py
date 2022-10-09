# P1-5: Graph1 DFS-Recursion by using MATRIX.  (Osman Bulut-001530539)
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

#my initial parameters must be outside of the function. Bcs we will use recursion.
visited = [11]   #source node is pre-visited. 11 is matrix index representation of 's'
path = [6]    #goal node is in the return path as given state.6 is matrix index representation of 'G'
parents = {11: 'None'}  #parent of source node is none


def dfs(graph, source, goal):
    for i in range(len(graph)):  #I'll consider the number of the codes to determine the 1 s to detect children
        if goal in visited:  # this is the condition of break of all the loop
            break
        else:
            if graph[source][i] == 1:
                if not i in visited:
                    visited.append(i)
                    parents[i] = source

                    if goal in visited:  # this is the condition of creating return path by using parents
                        l = goal
                        while not path[-1] == 11:
                            path.append(parents[l])
                            l = path[-1]

                    else:
                        dfs(g1matrix, i, goal)  # RECURSION line


dfs(g1matrix,11,6)  #graph, source and goal node are my inputs. 6 is node 'G' and 11 is node 's' in terms of the matrix.


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