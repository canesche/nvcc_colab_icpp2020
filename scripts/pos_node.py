import sys
import networkx as nx
from graphviz import Source

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))
	
    type_graph = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']

    pos = nx.drawing.nx_agraph.graphviz_layout(g, prog=type_graph[1])

    print(pos)

