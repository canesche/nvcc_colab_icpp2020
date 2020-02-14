import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

from graphviz import Source

def create_id(g, EDGE):
    dic_id = {}

    OPEN = []
    # get the node inputs
    cont_no = 0
    for n in g.nodes():
        cont_no += 1
        if g.in_degree(n) == 0:
            OPEN.insert(0,n)

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
    return dic_id, cont_no, len(EDGE)

def print_graph(g, get_position):

    label, x_pos, y_pos = [], [], []
    for i in get_position:
        label.append(i)
        x_pos.append(get_position[i][0])
        y_pos.append(get_position[i][1])
        print("Node: " + i +" x = "+ str(get_position[i][0]) +" y = "+ str(get_position[i][1]))

    fig, ax = plt.subplots()
    ax.scatter(x_pos, y_pos)

    for i, txt in enumerate(label):
        ax.annotate(txt, (x_pos[i], y_pos[i]))

    plt.show()

def placement():

    pass

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dict_id, SIZE_NODE, SIZE_EDGE = create_id(g, EDGE)

    print(EDGE)
	
    type_graph = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']
    get_position = nx.drawing.nx_agraph.graphviz_layout(g, prog=type_graph[1])

    #print_graph(g, get_position)

    print(SIZE_NODE)
    print(SIZE_EDGE)

    MAX_Y = math.ceil(math.sqrt(SIZE_NODE))
    MAX_X = math.ceil(math.sqrt(SIZE_NODE))

    print(MAX_Y)
