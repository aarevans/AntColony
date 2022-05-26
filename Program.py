from Graph import *
from Ant import *

#Create a non directed graph with 5 nodes.
graph = Graph(5, directed=False)

#Adds all edges to our graph matrix
graph.add_edge(0, 1, 3)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 3)
graph.add_edge(3, 4, 2)

#outputs the graph matrix
#graph.print_adj_matrix()

#create a list of n ants, this can be increased.
n = 3
#ants = [[]*3]
ants=[[0 for j in range(n)]for i in range(n)]
for x in range(n):
    ants[x] = Ant(str(x+1))

#foreach 
#for ant in ants:
ants[0].path = ants[0].FindPath(graph,0,4)
print(ants[0].path)
