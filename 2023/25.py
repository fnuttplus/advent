from sys import stdin
from math import prod
import networkx as nx
import matplotlib.pyplot as plt

nodes = set()
edges = set()

for line in stdin.read().splitlines():
    a,b = line.split(': ')
    nodes.add(a)
    for c in b.split(' '):
        nodes.add(c)
        edges.add((a,c))

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
#nx.draw(G, with_labels=True)
#plt.savefig("advent.png")
G.remove_edges_from(nx.minimum_edge_cut(G))
print(prod([len(x) for x in nx.connected_components(G)]))
