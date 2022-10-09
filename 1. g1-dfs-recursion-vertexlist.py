# P1-1: Graph1 DFS-Recursion by using VERTEX LIST.  (Osman Bulut-001530539)

g1 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'c', 'e', 's'],
    'e': ['d', 'h', 'r', 's'],
    'f': ['c', 'G', 'r'],
    'G': ['f'],
    'h': ['e', 'p', 'q'],
    's': ['d', 'e', 'p'],
    'p': ['h', 'q', 's'],
    'q': ['h', 'p'],
    'r': ['e', 'f']
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
            if not i in visited:
                visited.append(i)
                parents[i] = source

                if goal in visited:        #this is the condition of creating return path by using parents
                    l = goal
                    while not path[-1] == 's':
                        path.append(parents[l])
                        l = path[-1]

                else:
                    dfs(g1, i, goal)   #RECURSION line

dfs(g1, 's', 'G')  #graph data, source node and goal node are my inputs o the function

print('The return path is ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)