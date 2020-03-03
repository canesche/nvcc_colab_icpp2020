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

def print_grid(grid, GRID_SIZE, GRID_TOTAL_SIZE):
    print()
    for i in range(GRID_TOTAL_SIZE):
        if i % GRID_SIZE == 0:
            print()
        print("%4d" %grid[i], end="")
    print("\n")

def place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET):

    pos_b_x = pos_x[num_b] 
    pos_b_y = pos_y[num_b]
    
    print("\ntry POS_B", num_b)
    if (pos_b_x == 255):
        for i in range(TAM_OFFSET):
            pos_b_x = pos_a_x + offset_x[i]
            pos_b_y = pos_a_y + offset_y[i]

            print("X = %d Y = %d" %(pos_b_x,pos_b_y))

            pos_node = pos_b_x*GRID_SIZE + pos_b_y
            if (pos_b_x >= 0 and pos_b_y >= 0 and pos_b_x < GRID_SIZE and pos_b_y < GRID_SIZE and grid[pos_node] == 255):
                grid[pos_node] = num_b
                pos_x[num_b] = pos_b_x
                pos_y[num_b] = pos_b_y
                return True
    return False

def func_key(val1, val2):
    return str(val1) + " " + str(val2)

def func_unkey(string):
    return string.split(" ")

def smart_tranversal_algorithm(g, dict_id, EDGE, N_NODE):
    
    OutputList = []
    # get the node inputs
    for n in g.nodes():
        if g.out_degree(n) == 0:
            if (n == 'EXP_79'):
                OutputList.insert(0, [n, 'IN'])
            else:
                OutputList.append([n, 'IN'])
    
    GRID_SIZE = int(math.ceil(math.sqrt(N_NODE)))
    pos_x = np.full(N_NODE, 255)
    pos_y = np.full(N_NODE, 255)
    grid = np.full(GRID_SIZE*GRID_SIZE, 255)

    offset_x = [0, 0, 1, 0,-1]
    offset_y = [0, 1, 0,-1, 0]
    TAM_OFFSET = len(offset_x)

    Stack = OutputList.copy()
    VISITED = []
    EDGES = []
    CYCLE = []

    L_fanin = {}
    L_fanout = {}
    for no in g:
        L_fanin[no] = list(g.predecessors(no))
        L_fanout[no] = list(g.successors(no))

    while Stack:
        #print("Stack:", Stack)

        a, direction = Stack.pop(0) # get the top1

        fanin = len(L_fanin[a])     # get size fanin
        fanout = len(L_fanout[a])    # get size fanout

        if direction == 'IN': # direction == 'IN'
            
            if fanout >= 1: # Case 3

                #print("-----------------------------------------------CASE 3 IN")
                #print("Fanin:", L_fanin[a])
                #print("Fanout:", L_fanout[a])

                b = L_fanout[a][-1] # get the element more the right side

                Stack.insert(0, [a, 'IN'])
                Stack.insert(0, [b, 'OUT'])
                
                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])
                else:
                    CYCLE.append([a,b])
                    print(b)
                print("%s -> %s Case %d IN" %(a, b, 3))

                #print("Change direction")

            elif fanin == 1: # Case 1
                #print("-----------------------------------------------CASE 1 IN")
                #print("Fanin:", L_fanin[a])
                # Place the element in 'b'
                
                b = L_fanin[a][0] # just have 1 element (fanin == 1)
                
                Stack.insert(0, [b, 'IN'])
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                else:
                    CYCLE.append([a,b])
                    print(b)
                print("%s -> %s Case %d IN" %(a, b, 1))
            
            elif fanin > 1: # Case 2
                #print("-----------------------------------------------CASE 2 IN")
                #print("Fanin:", L_fanin[a])
                
                b = L_fanin[a][-1]      # get the elem more in the right
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                else: 
                    CYCLE.append([a,b])
                    print(b)
                Stack.insert(0, [b, 'IN'])
                print("%s -> %s Case %d IN" %(a, b, 2))        

        else: # direction == 'OUT'
            
            if fanin >= 1: # Case 3

                #print("-----------------------------------------------CASE 3 OUT")
                #print("Fanin:", L_fanin[a])
                #print("Fanout:", L_fanout[a])

                b = L_fanin[a][0] # get the element more left side

                Stack.insert(0, [a, 'OUT'])
                Stack.insert(0, [b, 'IN'])
                
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                else:
                    CYCLE.append([a,b])
                    print(b)
                print("%s -> %s Case %d OUT" %(a, b, 3))

            elif (fanout == 1): # Case 1
                #print("-----------------------------------------------CASE 1 OUT")
                #print("Fanout:", L_fanout[a])
                # Place the element in 'b'

                b = L_fanout[a][0] # just have 1 element (fanout == 1)
                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])
                else:
                    CYCLE.append([a,b])
                    print(b)
                Stack.insert(0, [b, 'OUT']) # put b on the top
                print("%s -> %s Case %d OUT" %(a, b, 1))
            
            elif fanout > 1: # Case 2
                #print("-----------------------------------------------CASE 2 OUT")
                #print("Fanout:", L_fanout[a])
                
                b = L_fanout[a][0]  # get the element more left side

                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])
                else:
                    CYCLE.append([a,b])
                    print(b)

                Stack.insert(0, [b, 'OUT']) # put b on the top
                print("%s -> %s Case %d OUT" %(a, b, 2))
        
        VISITED.append(a)
        #print_grid(grid, GRID_SIZE, len(grid))
        #print("vector pos_x:", pos_x)
        #print("vector pos_y:", pos_y)
        #print()
    
    dic_CYCLE = {}
    # Initialization dictionary
    for i in range(len(EDGES)):
        key = func_key(EDGES[i][0],EDGES[i][1])
        dic_CYCLE[key] = []
        print(EDGES[i])
    
    print(CYCLE)
    for i in range(len(CYCLE)):
        found_start = False
        count = 0
        value1 = ''
        elem_cycle_begin = CYCLE[i][0]
        elem_cycle_end = CYCLE[i][1]
        walk_key = []
        for j in range(len(EDGES)-1,-1,-1):
            
            if EDGES[j][1] == elem_cycle_begin and not found_start:
                value1 = EDGES[j][0]
                key = func_key(EDGES[j][0],EDGES[j][1])
                walk_key.insert(0, key)
                dic_CYCLE[key].append([elem_cycle_end, count])
                count += 1
                found_start = True

            elif found_start and (value1 == EDGES[j][1] or EDGES[j][0] == elem_cycle_end or EDGES[j][1] == elem_cycle_end):
                value1 = EDGES[j][0]
                value2 = EDGES[j][1]
                key = func_key(EDGES[j][0],EDGES[j][1])

                if EDGES[j][0] != elem_cycle_end and EDGES[j][1] != elem_cycle_end:
                    walk_key.insert(0, key) 
                    dic_CYCLE[key].append([elem_cycle_end, count])
                    count += 1

                if value1 == elem_cycle_end or value2 == elem_cycle_end:
                    found_start = False
                    # Go back and update values
                    for k in range(0, count//2):
                        dic_actual = dic_CYCLE[walk_key[k]]
                        for l in range(len(dic_actual)):
                            if (dic_actual[l][0] == elem_cycle_end):
                                dic_CYCLE[walk_key[k]][l][1] = k
                    break # to the next on the vector CYCLE
        #break
    
    print(dic_CYCLE)

    for key in dic_CYCLE:
        print(key, ": ", dic_CYCLE[key])


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)
    
    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dic_id, N_NODE, N_EDGE = create_id(g, EDGE)

    #print(str(N_NODE) + " " + str(N_EDGE) + "\n")

    smart_tranversal_algorithm(g, dic_id, EDGE, N_NODE)
