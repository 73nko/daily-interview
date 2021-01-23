###
# 04-12-2020
# Hi, here's your problem today. This problem was recently asked by Facebook:
# Given an undirected graph, determine if a cycle exists in the graph.
###

def find_cycle(graph):
    visited = {}
    for vertex in graph.keys():
        if not vertex in visited:
            if find(graph[vertex], vertex, visited):
                return True
    return False


def find(graph, vertex, visited):
    if vertex in visited:
        return True
    visited[vertex] = True
    for n in graph:
        if find(graph[n], n, visited):
            return True
    return False


graph = {
    'a': {'a2': {}, 'a3': {}},
    'b': {'b2': {}},
    'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
