import sys
import networkx as nx

if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        number_node = int(sys.argv[1])
        number_tree = int(sys.argv[2])
        if number_node < 1:
            print("Number of nodes is greater than 0")
            exit(0)
    else:
        print("python3 generate_tree_dot.py <number_node> <number_tree>\n")
        exit(0)

    count = 0
    qtd = 2  # tree binary
    
    g = nx.DiGraph()

    for k in range(number_tree):
        list_node = []
        for i in range(qtd):
            list_node.append(count)

        for i in range(0,number_node-1):
            count += 1
            #g.add_node(count)
            for j in range(qtd):
                list_node.append(count)
            node = list_node.pop(0)
            g.add_edge(node, count)
        count += 1
    
    #print(g.nodes)
    #print(g.edges)
    #print(list_node)

    nx.drawing.nx_pydot.write_dot(g, "../dot/tree_n_"+str(number_node)+"_t_"+str(number_tree)+".dot")