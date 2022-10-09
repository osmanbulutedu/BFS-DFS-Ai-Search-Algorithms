# P1-4: Graph1 BFS-Stack by using VERTEX LIST.  (Osman Bulut-001530539)

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


def bfs(graph, source, goal):  # my function's input will be graph data, source node, and goal node.
    # initial parameters
    visited = {}
    stack = [source]
    expanded = []
    path = [goal]
    parents = {source: 'none'}
    for i in graph.keys():  # None of the nodes is visited yet. So I'll assign False for all nodes
        visited[i] = False

    visited[source] = True  # only source node will be accepted as visited

    # Now, I'll create a loop. I'll iterate this loop as long as there is an item in the stack and not arriving the goal node.

    while not stack == [] and goal not in expanded:
        k = stack.pop(0)

        expanded.append(k)

        # I'll create another loop which will check out the neighbors of my last visited node one by one.
        # If the nodes are not visited, they will be added to queue stack, and assigned as visited.
        for i in graph[k]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    # Our expanded nodes list is ready

    # in order to obtain return path, I'll first determine the parents of each node.
    for j in range(len(expanded)):
        for i in graph[expanded[j]]:
            if not i in parents:
                parents[i] = expanded[j]
    # now we can follow track the parents starting from the goal
    if goal in parents:
        i = goal
        while not path[-1] == source:
            path.append(parents[i])
            i = path[-1]

    return (expanded, list(reversed(path)))


expanded, returnpath = bfs(g1, 's', 'G')  # I put graph data, source node info and goal node info into my function
print('BFS Expanded Vertices until finding the goal node is ---->', expanded)
print('Return path is ----> ', returnpath)
