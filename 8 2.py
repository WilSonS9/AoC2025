import networkx as nx
import math

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

G = nx.Graph()
for r in l:
    x, y, z = map(int, r.split(','))
    G.add_node((x, y, z))

def dist(n1, n2):
    x1, y1, z1 = n1
    x2, y2, z2 = n2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

distances = []
covered_pairs = set()

for n1 in G.nodes:
    for n2 in G.nodes:
        if n1 == n2 or (n2, n1) in covered_pairs:
            continue
        distances.append((n1, n2, dist(n1, n2)))
        covered_pairs.add((n1, n2))

distances.sort(key=lambda triple: triple[2])

while True:
    n1, n2, _ = distances.pop(0)
    G.add_edge(n1, n2)
    n_connected_components = nx.number_connected_components(G)
    if n_connected_components == 1:
        x1 = n1[0]
        x2 = n2[0]
        print(x1 * x2)
        break
