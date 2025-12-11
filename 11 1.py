import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

G = nx.DiGraph()
for r in l:
    node, neighbours_s = r.split(': ')
    neighbours = neighbours_s.split(' ')
    for neighbour in neighbours:
        G.add_edge(node, neighbour)

source = 'you'
target = 'out'
paths = nx.all_simple_paths(G, source, target)
n_paths = sum(1 for _ in paths)

print(n_paths)
