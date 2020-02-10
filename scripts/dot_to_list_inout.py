import sys
import networkx as nx
from graphviz import Source

def create_id(g, EDGE):
    
    dic_id = {}

    OPEN = []
    INPUT, OUTPUT = [], []
    # get the node inputs
    cont_no = 0
    for n in g.nodes():
        cont_no += 1
        if g.in_degree(n) == 0:
            OPEN.insert(0,n)
            INPUT.append(n)
        if g.out_degree(n) == 0:
            OUTPUT.append(n)

    CLOSED = []

    count = 0
    while len(OPEN) > 0 :
        node = OPEN.pop()
        CLOSED.append(node)
        dic_id[node] = count

        for no in list(g.successors(node)):
            EDGE.append([node, no]) 
            if no not in OPEN and no not in CLOSED:
                OPEN.insert(0, no)
        count += 1 

    print(str(count)+" "+str(len(EDGE))+"\n")
    for i in range(len(EDGE)):
        print(str(dic_id[EDGE[i][0]])+" "+str(dic_id[EDGE[i][1]]))
    
    print()
    for i in range(len(INPUT)):
        print(dic_id[INPUT[i]])
    for i in range(len(OUTPUT)):
        print(dic_id[OUTPUT[i]])  

    return dic_id, count, len(EDGE)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)
    
    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dic_id, N_NODE, N_EDGE = create_id(g, EDGE)
