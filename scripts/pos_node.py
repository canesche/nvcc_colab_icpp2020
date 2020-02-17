import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import time

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

def print_graph(x_pos, y_pos, node, label):

    fig, ax = plt.subplots()
    ax.scatter(x_pos, y_pos)

    print(label)

    for i, txt in enumerate(node):
        ax.annotate(label[0][i], (x_pos[i], y_pos[i]))

    plt.show()

'''
def method_shift(conflict_node, GRID, x_new, y_new):
    while len(conflict_node) > 0:
        
        node = conflict_node.pop(0)
        pos_x, pos_y = x_new[node], y_new[node]

        # try place on neighborhood
        elif pos_x+1 < len(GRID[0]) and GRID[pos_x+1][pos_y] == -1:
            x_new[node] = pos_x + 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x-1 >= 0 and GRID[pos_x-1][pos_y] == -1:
            x_new[node] = pos_x - 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y+1 < len(GRID[0]) and GRID[pos_x][pos_y+1] == -1:
            y_new[node] = pos_y + 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y-1 >= 0 and GRID[pos_x][pos_y-1] == -1:
            y_new[node] = pos_y - 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x+2 < len(GRID[0]) and GRID[pos_x+2][pos_y] == -1:
            x_new[node] = pos_x + 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x-2 >= 0 and GRID[pos_x-1][pos_y] == -1:
            x_new[node] = pos_x - 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y+2 < len(GRID[0]) and GRID[pos_x][pos_y+2] == -1:
            y_new[node] = pos_y + 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y-2 >= 0 and GRID[pos_x][pos_y-2] == -1:
            y_new[node] = pos_y - 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        
        print("cheguei aqui!!!")
        # shift
        for i in range(len(GRID[0]),,-1)
        # try the method here
        # thinking ...

    return GRID, x_new, y_new 
'''
def method_splash(conflict_node, GRID, x_new, y_new):
    while len(conflict_node) > 0:
        
        node = conflict_node.pop(0)
        pos_x, pos_y = x_new[node], y_new[node]

        # try place on neighborhood
        if pos_x+1 < len(GRID[0]) and GRID[pos_x+1][pos_y] == -1:
            x_new[node] = pos_x + 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x-1 >= 0 and GRID[pos_x-1][pos_y] == -1:
            x_new[node] = pos_x - 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y+1 < len(GRID[0]) and GRID[pos_x][pos_y+1] == -1:
            y_new[node] = pos_y + 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y-1 >= 0 and GRID[pos_x][pos_y-1] == -1:
            y_new[node] = pos_y - 1
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x+2 < len(GRID[0]) and GRID[pos_x+2][pos_y] == -1:
            x_new[node] = pos_x + 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_x-2 >= 0 and GRID[pos_x-1][pos_y] == -1:
            x_new[node] = pos_x - 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y+2 < len(GRID[0]) and GRID[pos_x][pos_y+2] == -1:
            y_new[node] = pos_y + 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        elif pos_y-2 >= 0 and GRID[pos_x][pos_y-2] == -1:
            y_new[node] = pos_y - 2
            GRID[x_new[node]][y_new[node]] = node
            continue
        
        for i in range(len(GRID//2)):
            found = False
            for j in range(len(GRID//2)):
                if (GRID[i][j] == -1):
                    x_new[node], y_new[node] = i, j
                    GRID[i][j] = node
                    found = True
                    break
            if (found):
                print("cheguei aqui!!! %d" %node)
                break
        # try the method here

    return GRID, x_new, y_new 

def function_cost_1hop(x, y, dict_id, EDGE):

    cost = 0

    for i in range(len(EDGE)):
        if EDGE[i][0] == EDGE[i][1]:
            continue
        diff_x = abs(x[dict_id[EDGE[i][0]]] - x[dict_id[EDGE[i][1]]])
        diff_y = abs(y[dict_id[EDGE[i][0]]] - y[dict_id[EDGE[i][1]]])
        cost_local = diff_x // 2 + diff_x % 2 + diff_y // 2 + diff_y % 2 - 1
        cost += cost_local
        print("%2d [%2d,%2d] -> %2d [%2d,%2d] Cost: %2d" %(dict_id[EDGE[i][0]], x[dict_id[EDGE[i][0]]], y[dict_id[EDGE[i][0]]], dict_id[EDGE[i][1]], x[dict_id[EDGE[i][1]]], y[dict_id[EDGE[i][1]]], cost_local))
    return cost

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dict_id, SIZE_NODE, SIZE_EDGE = create_id(g, EDGE)
	
    type_graph = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']

    for k in range(len(type_graph)):

        print("\n\nTYPE: %s\n" %type_graph[k])

        get_position = nx.drawing.nx_agraph.graphviz_layout(g, prog=type_graph[k])

        print(get_position)

        GRID_SIZE = math.ceil(math.sqrt(SIZE_NODE))

        node, x_pos, y_pos = [], [], []
        label = np.full((1,SIZE_NODE), 'xxxxxxxx')
        
        for i in get_position:
            label[0][dict_id[i]] = i
            node.append(dict_id[i])
            x_pos.append(get_position[i][0])
            y_pos.append(get_position[i][1])
            #print("Node: " + i +" x = "+ str(get_position[i][0]) +" y = "+ str(get_position[i][1]))

        MAX_X, MAX_Y = max(x_pos), max(y_pos)

        x_new, y_new = [], []
        for i in range(len(node)):
            x_new.append(int((GRID_SIZE-1) * x_pos[node[i]] // MAX_X))
            y_new.append(int((GRID_SIZE-1) * y_pos[node[i]] // MAX_Y))
        
        #for i in range(len(label)):
        #    print("%8s: [%2d,%2d]" % (label[i], x_new[label[i]], y_new[label[i]]))

        #print_graph(x_new, y_new, node, label)

        start = time.clock()
        GRID = np.full((GRID_SIZE,GRID_SIZE),-1)
        
        conflict_node = []
        # verify conflict and correct then
        for i in range(len(node)):
            if GRID[x_new[node[i]]][y_new[node[i]]] == -1:
                GRID[x_new[node[i]]][y_new[node[i]]] = node[i]
            else: # conflict
                # save to future, and then choice a new place
                conflict_node.append(node[i])

        print("Conflict: ", conflict_node)
        time_placement = time.clock() - start

        start = time.clock()
        new_GRID, m1_x_new, m1_y_new = method_splash(conflict_node.copy(), GRID.copy(), x_new.copy(), y_new.copy())
        time_conflict = time.clock() - start

        #print_graph(m1_x_new, m1_y_new, node, label)

        print(new_GRID)
        print()
        cost_m1 = function_cost_1hop(m1_x_new, m1_y_new, dict_id, EDGE)

        print("Cost 1-hop: %d" %cost_m1)
        print("Time (place&conflict) %.4f ms"%(time_placement*1000+time_conflict*1000))