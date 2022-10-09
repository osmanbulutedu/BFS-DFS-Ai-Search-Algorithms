# P1-2: Graph1 DFS-Stack by using VERTEX LIST.  (Osman Bulut-001530539)

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


dfs(g1, 's','G')  # graph data, source, and goal node as list, and visited initial parameter are my inputs
print('The return path is ----> ', list(reversed(path)))
print("The expanded vertex list until reaching the destination is ---->", visited)


