from sys import stdin
from aocd import get_data, submit, puzzle
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *
from oklab import viridis, _viridis_data
from math import prod
import networkx as nx
import matplotlib.pyplot as plt

t = False
#t = True

nodes = set()
edges = set()
ls = puzzle.examples[0].input_data if t else get_data(day=23)

for line in ls.splitlines():
    a,b = line.split('-')
    nodes.add(a)
    nodes.add(b)
    edges.add((a,b))

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

#find all complete subgraphs of size 3
def find_subgraphs(G):
    for ss in nx.enumerate_all_cliques(G):
        if len(ss) == 3:
            # if any nodes name starts with t
            if any([s.startswith('t') for s in ss]):
                yield tuple(sorted(ss))

s = len(set(find_subgraphs(G)))
print('part 1',s)

#find largest clique
def find_largest_clique(G):
    return max(nx.find_cliques(G), key=len)

c = find_largest_clique(G)
s = ','.join(sorted(c))
print('part 2',s)

# draw graph
v = _viridis_data
color_map = []
for node in G:
    if node.startswith('t'):
        color_map.append(v[100])
    elif node in c:
        color_map.append(v[240])
    else:
        color_map.append(v[50])

sg = list(find_subgraphs(G))
sedges = set([e for subgraph in sg for e in G.subgraph(subgraph).edges])
edge_colors = []
for edge in G.edges:
    if (edge[0],edge[1]) in sedges or (edge[1],edge[0]) in sedges:
        edge_colors.append(v[150])
    else:
        edge_colors.append(v[50])

pos = nx.spring_layout(G, k=0.15)
nx.draw(G, with_labels=True, pos=pos, font_size=3, width=0.1, node_size=10, node_color=color_map, edge_color=edge_colors, font_color='black')
plt.savefig("23.png", dpi=300, transparent=True, pad_inches=0.0, bbox_inches='tight')


if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    print(s)
