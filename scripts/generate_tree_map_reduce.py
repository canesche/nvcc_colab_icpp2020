import sys
import networkx as nx

if __name__ == "__main__":
    
    if len(sys.argv) > 3:
        number_node = int(sys.argv[1])
        number_tree = int(sys.argv[2])
        node_reduce = int(sys.argv[3])
        if number_node < 1:
            print("Number of nodes is greater than 0")
            exit(0)
    else:
        print("python3 generate_tree_dot.py <number_node> <number_tree> <node_reduce>\n")
        exit(0)

    count = 0
    qtd = 2  # tree binary
    
    g = nx.DiGraph()

    before = []
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
    
        # get the leaf
        leaf = []
        for node in g.nodes():
            #print(node)
            if len(list(g.successors(node))) == 0:
                if node not in before:
                    leaf.append(node)
        
        for i in range(len(leaf)):
            print(leaf[i], count)
            g.add_edge(leaf[i], count)
            for j in range(node_reduce-1):
                print(count, count+1)
                g.add_edge(count, count+1)
                count += 1
            before.append(count)
            count += 1

        for i in range(len(leaf)):
            before.append(leaf[i])
    #print(g.nodes)
    #print(g.edges)
    #print(list_node)

    nx.drawing.nx_pydot.write_dot(g, "dot/tree_n_"+str(number_node)+"_t_"+str(number_tree)+"_r_"+str(node_reduce)+".dot")
