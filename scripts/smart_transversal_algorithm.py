import sys
import networkx as nx
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
    return dic_id, count, len(EDGE)

def smart_tranversal_algorithm(g, dict_id, EDGE, N_NODE):
    
    OutputList = []
    # get the node inputs
    for n in g.nodes():
        if g.out_degree(n) == 0:
            OutputList.append(n)

    print(OutputList)
    GRID_SIZE = int(math.ceil(math.sqrt(N_NODE)))
    pos_x = np.full(N_NODE, 255)
    pos_y = np.full(N_NODE, 255)
    grid = np.full(GRID_SIZE*GRID_SIZE, 255)

    offset_x = [0, 0, 1, 0,-1]
    offset_y = [0, 1, 0,-1, 0]
    TAM_OFFSET = len(offset_x)

    print("vector pos_x:", pos_x)

    Stack = OutputList.copy()

    while Stack:
        a = Stack.pop(0) # get the top
        num_a = dict_id[a]
        print(num_a)
        pos_a_x = pos_x[num_a] 
        pos_a_y = pos_y[num_a]
        
        if pos_x[num_a] == 255:
            # Place the element in 'a'
            pos_x[num_a] = pos_a_x = 0
            pos_y[num_a] = pos_a_y = 0
            pos_node = pos_a_x*GRID_SIZE + pos_a_y
            grid[pos_node] = num_a

        # get fanin
        L = list(g.predecessors(a))
        fanin = g.in_degree(a)
        
        if (fanin == 1): # Case 1
            # Place the element in 'b'
            b = L[0] # just have 1 element
            num_b = dict_id[b]
            pos_b_x = pos_x[num_b] 
            pos_b_y = pos_y[num_b]
            
            if (pos_b_x == 255):
                for i in range(TAM_OFFSET):
                    pos_b_x = pos_a_x + offset_x[i]
                    pos_b_y = pos_a_y + offset_y[i]

                    pos_node = pos_b_x*GRID_SIZE + pos_b_y
                    if (pos_b_x >= 0 and pos_b_y >= 0 and pos_b_x < GRID_SIZE and pos_b_y < GRID_SIZE and grid[pos_node] == 255):
                        grid[pos_node] = num_b
                        pos_x[num_b] = pos_b_x
                        pos_y[num_b] = pos_b_y
                        break
            Stack.insert(0, b) # put b on the top
        
        elif fanin == 2:
            pass

        print(Stack)
        print(grid)
        print(pos_x)
        print(pos_y)
        print() 
        break

        


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)
    
    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dic_id, N_NODE, N_EDGE = create_id(g, EDGE)

    print(str(N_NODE) + " " + str(N_EDGE) + "\n")

    smart_tranversal_algorithm(g, dic_id, EDGE, N_NODE)