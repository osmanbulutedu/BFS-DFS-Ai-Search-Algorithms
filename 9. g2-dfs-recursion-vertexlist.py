# P1-9: Graph2 DFS-Recursion by using VERTEX LIST.  (Osman Bulut-001530539)

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
visited = ['s']   #source node is previsited
path = ['G']    #goal node is in the return path as given state
parents = {'s': 'None'}  #parent of source node is none


def dfs(graph, source, goal):
    for i in graph[source]:
        if goal in visited: #this is the condition of break of all the loop
            break
        else:
            if not i in visited and i not in source:
                visited.append(i)
                parents[i] = source

                if goal in visited:        #this is the condition of creating return path by using parents
                    l = goal
                    while not path[-1] == 's':
                        path.append(parents[l])
                        l = path[-1]

                else:
                    dfs(g2, i, goal)   #RECURSION line

dfs(g2, 's', 'G')  #graph data, source node and goal node are my inputs o the function

print('The return path is ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)