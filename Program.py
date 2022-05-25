import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

#create nodes
G.add_nodes_from(['A','B','C','D','E'])

# Use add_edges_from to add pairwise relationships
G.add_edge('B','C',weight=0.5)
G.add_edge('A','C',weight=0.5)
G.add_edge('B','D',weight=0.5)
G.add_edge('D','A',weight=0.5)
G.add_edge('D','E',weight=0.5)
G.add_edge('B','E',weight=0.5)

print(G.nodes())
print(G.edges())

pos=nx.spring_layout(G)

#pos=nx.get_node_attributes(G,'pos')

nx.draw(G,pos)

labels = nx.get_edge_attributes(G,'weight')

nx.draw_networkx_labels(G,pos,edge_labels=labels,with_labels=True)

plt.savefig("graph.png")

