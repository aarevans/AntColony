class Ant:
    def __init__(this,instance):
        this.number = instance
        this.path = []

    def FindPath(this,graph,start,finish):
        #for i in range(graph.m_num_of_nodes):
        best_option = 0
        path_taken = ""
        for option in graph.m_adj_matrix[start]:
            if option > best_option:
                best_option = option
                
        return best_option