import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

#create nodes
G.add_nodes_from(['A','B','C','D','E'])

# Use add_edges_from to add pairwise relationships
G.add_edge('B','C',weight=1)
G.add_edge('A','C',weight=1)
G.add_edge('B','D',weight=1)
G.add_edge('D','A',weight=1)
G.add_edge('D','E',weight=1)
G.add_edge('B','E',weight=1)

#print(G.nodes())
#print(G.edges())

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

