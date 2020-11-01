import sys
import networkx as nx
from graphviz import Source

def create_dot(path_blif, name):

    with open(path_blif, "r") as f:
        data = f.read()

    edges = []
    
    for line in data.split("\n"):
        #print(line)
        if ".names" in line:
            d = line.replace('[','"[').replace(']',']"').split(" ")[1:]
            for i in range(len(d)-1):
                e = (d[i], d[-1])
                if e not in edges:
                    edges.append(e)
    
    print("digraph g {")
    for i in range(len(edges)):
        print(" %s -> %s" %(edges[i][0], edges[i][1]))
    print("}")

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        blif = sys.argv[1]
    else:
        print("python3 blif_to_dot.py <name.blif>\n")
        exit(0)
    
    name = blif.split(".")[0]
    
    create_dot(blif, name)
