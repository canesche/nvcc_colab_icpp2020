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
    VISITED = [OutputList[0][0]]
    Unvisited_Fanin = []

    while Stack:
        print("Stack:", Stack)

        a, direction = Stack.pop(0) # get the top
        num_a = dict_id[a]
        print("Node a = %s number %d dir %s" %(a, num_a, direction))
        
        pos_a_x = pos_x[num_a] 
        pos_a_y = pos_y[num_a]
        
        if pos_x[num_a] == 255:
            # Place the element in 'a'
            pos_x[num_a] = pos_a_x = 0
            pos_y[num_a] = pos_a_y = 0
            pos_node = pos_a_x*GRID_SIZE + pos_a_y
            grid[pos_node] = num_a

        if direction == 'IN': # direction == 'IN'
            
            L_fanin = list(g.predecessors(a)) # get elem fanin
            fanin = g.in_degree(a)      # get size fanin
            fanout = g.out_degree(a)    # get size fanout
            
            if fanout > 1: # Case 3
                L_fanout = list(g.successors(a)) # get elem fanin

                print("-----------------------------------------------CASE 3 IN")
                print("Fanin:", L_fanin)
                print("Fanout:", L_fanout)

                for elem in L_fanin:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'IN'])
                
                get_elem = False
                for elem in L_fanout:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'OUT'])
                        b = elem                # get the last elem not visited
                        get_elem = True

                if not get_elem:
                    print("Already visited")
                    continue
                VISITED.append(b)       # PUT b visited

                num_b = dict_id[b]
                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
                print("Change direction")

            elif fanin == 1: # Case 1
                print("-----------------------------------------------CASE 1 IN")
                print("Fanin:", L_fanin)
                # Place the element in 'b'
                
                b = L_fanin[0] # just have 1 element (fanin == 1)
                if b in VISITED:
                    print("Already visited")
                    continue
                VISITED.append(b)          # PUT b visited
                
                Stack.insert(0, [b, 'IN']) # put b on the top
                
                num_b = dict_id[b]

                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
            
            elif fanin > 1 and fanout == 1: # Case 2
                print("-----------------------------------------------CASE 2 IN")
                print("Fanin:", L_fanin)
                
                get_elem = False
                for elem in L_fanin:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'IN'])
                        b = elem            #  # get the elem more in the right
                        get_elem = True
                
                if not get_elem:
                    print("Already visited")
                    continue
                VISITED.append(b)       # PUT b visited

                num_b = dict_id[b]
                print("GET b = %s number %d" %(b, num_b))

                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
            
            

        else: # direction == 'OUT'
            L_fanout = list(g.successors(a)) # get elem fanout
            fanin = g.in_degree(a)      # get size fanin
            fanout = g.out_degree(a)    # get size fanout

            if fanin > 1: # Case 3

                L_fanin = list(g.predecessors(a)) # get elem fanin

                print("-----------------------------------------------CASE 3 OUT")
                print("Fanin:", L_fanin)
                print("Fanout:", L_fanout)

                for elem in L_fanout:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'OUT'])
                
                get_elem = False
                for elem in L_fanin:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'IN'])
                        b = elem                # get the last elem not visited
                        get_elem = True

                if not get_elem:
                    print("Already visited")
                    continue
                VISITED.append(b)       # PUT b visited

                num_b = dict_id[b]
                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
                print("Change direction")

            elif (fanout == 1): # Case 1
                print("-----------------------------------------------CASE 1 OUT")
                print("Fanout:", L_fanout)
                # Place the element in 'b'

                b = L_fanout[0] # just have 1 element (fanout == 1)
                if b in VISITED:
                    print("Already visited")
                    continue
                VISITED.append(b)          # PUT b visited
                
                Stack.insert(0, [b, 'OUT']) # put b on the top
                
                num_b = dict_id[b]

                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
                VISITED.append(b)          # PUT b visited
            
            elif fanout > 1: # Case 2
                print("-----------------------------------------------CASE 2 OUT")
                print("Fanout:", L_fanout)
                
                get_elem = False
                for elem in L_fanout:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'OUT'])
                        b = elem            #  # get the elem more in the right
                        get_elem = True
                
                if not get_elem:
                    print("Already visited")
                    continue
                VISITED.append(b)       # PUT b visited
                
                num_b = dict_id[b]
                print("GET b = %s number %d" %(b, num_b))

                bool_place = place_b(num_b, pos_a_x, pos_a_y, pos_x, pos_y, grid, GRID_SIZE, offset_x, offset_y, TAM_OFFSET)

                if not bool_place:
                    print("Not place %s -> %s", a, b)
                    break
                VISITED.append(b)       # PUT b visited
        
        print_grid(grid, GRID_SIZE, len(grid))
        #print("vector pos_x:", pos_x)
        #print("vector pos_y:", pos_y)
        print()

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
