# P1-10: Graph2 DFS-Stack by using VERTEX LIST.  (Osman Bulut-001530539)

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

# I'll keep track visited set, and also total traversal and the path until finding the goal node
visited = []
path = ['G']
parents = {'s': 'None'} #source node dont have a parent


# I'll define my dfs function with using only stack.
# I'll get the visited list, vertice list information and the source node information to initialize the search.
def dfs(graph, source, goal):  # function for dfs
    stack=[source]
    while goal not in visited:  # instead of recursion I'll use a single while loop until hitting the goal node.
        expanded = stack.pop()
        if expanded not in visited:
            visited.append(expanded)

        for i in reversed(graph[expanded]):
            if not i in visited:
                stack.append(i)
                parents[i] = expanded #I'll save all expanded nodes' children

    # now we can follow track the parents starting from the goal
    if goal in parents:
        i = goal
        while not path[-1] == source:
            path.append(parents[i])
            i = path[-1]


dfs(g2, 's','G')  # graph data, source, and goal node as list, and visited initial parameter are my inputs
print('The return path is ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)


