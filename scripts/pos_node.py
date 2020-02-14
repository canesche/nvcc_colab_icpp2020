import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from graphviz import Source

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))
	
    type_graph = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']

    get_position = nx.drawing.nx_agraph.graphviz_layout(g, prog=type_graph[1])

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
