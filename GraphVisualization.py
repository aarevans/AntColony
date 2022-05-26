##This code is purely to create a visual representation of the graph we will be using 
##and will save this graph in a png file called graph.png.

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

#create nodes
G.add_nodes_from(['0','1','2','3','4'])

# Use add_edges_from to add pairwise relationships
G.add_edge('0','1',weight=3)
G.add_edge('0','2',weight=4)
G.add_edge('1','2',weight=2)
G.add_edge('1','3',weight=2)
G.add_edge('1','4',weight=3)
G.add_edge('3','4',weight=2)

#Creates the graph layout using all nodes and edges and stores in pos variable
pos=nx.spring_layout(G)

#pos=nx.get_node_attributes(G,'pos')

#creates visual representation of the graph (including labelling nodes)
nx.draw(G,pos, with_labels=True)

#Stores the weight values for each edge in a labales variable
labels = nx.get_edge_attributes(G,'weight')

#Adds edge labels for the weights to the graph
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

#Saves the created graph in a png file.
plt.savefig("graph.png")

