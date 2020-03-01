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
    VISITED = []
    EDGES = []

    L_fanin = {}
    L_fanout = {}
    for no in g:
        L_fanin[no] = list(g.predecessors(no))
        L_fanout[no] = list(g.successors(no))

    while Stack:
        print("Stack:", Stack)

        a, direction = Stack.pop(0) # get the top1

        fanin = len(L_fanin[a])     # get size fanin
        fanout = len(L_fanout[a])    # get size fanout

        if direction == 'IN': # direction == 'IN'
            
            if fanout >= 1: # Case 3

                print("-----------------------------------------------CASE 3 IN")
                print("Fanin:", L_fanin[a])
                print("Fanout:", L_fanout[a])

                b = L_fanout[a][-1] # get the element more the right side

                Stack.insert(0, [a, 'IN'])
                Stack.insert(0, [b, 'OUT'])
                
                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])
                print("a -> b", a, b)

                print("Change direction")

            elif fanin == 1: # Case 1
                print("-----------------------------------------------CASE 1 IN")
                print("Fanin:", L_fanin[a])
                # Place the element in 'b'
                
                b = L_fanin[a][0] # just have 1 element (fanin == 1)
                '''
                if b in VISITED:
                    print("Already visited")
                    continue
                Stack.insert(0, [b, 'IN'])
                VISITED.append(b)          # PUT b visited
                '''
                Stack.insert(0, [b, 'IN'])
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                print("a -> b",a, b)
            
            elif fanin > 1: # Case 2
                print("-----------------------------------------------CASE 2 IN")
                print("Fanin:", L_fanin[a])
                '''
                get_elem = False
                for elem in L_fanin[a]:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'IN'])
                        b = elem            #  # get the elem more in the right
                        get_elem = True
                
                if not get_elem:
                    print("Already visited")
                    continue
                '''
                b = L_fanin[a][-1]      # get the elem more in the right
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                Stack.insert(0, [a, 'IN'])
                Stack.insert(0, [b, 'IN'])
                print("a -> b",a, b)           

        else: # direction == 'OUT'
            
            if fanin >= 1: # Case 3

                print("-----------------------------------------------CASE 3 OUT")
                print("Fanin:", L_fanin[a])
                print("Fanout:", L_fanout[a])

                '''
                for elem in L_fanout[a]:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'OUT'])
                
                get_elem = False
                for elem in L_fanin[a]:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'IN'])
                        b = elem                # get the last elem not visited
                        get_elem = True

                if not get_elem:
                    print("Already visited")
                    continue
                Stack.insert(1, [a, 'OUT'])

                VISITED.append(b)       # PUT b visited
                '''

                b = L_fanin[a][0] # get the element more left side

                Stack.insert(0, [a, 'OUT'])
                Stack.insert(0, [b, 'IN'])
                
                L_fanin[a].remove(b)
                L_fanout[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'I'])
                print("a -> b",a, b)

            elif (fanout == 1): # Case 1
                print("-----------------------------------------------CASE 1 OUT")
                print("Fanout:", L_fanout[a])
                # Place the element in 'b'

                '''
                b = L_fanout[a][0] # just have 1 element (fanout == 1)
                if b in VISITED:
                    print("Already visited")
                    continue

                VISITED.append(b)          # PUT b visited
                '''
                b = L_fanout[a][0] # just have 1 element (fanout == 1)
                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])
                
                Stack.insert(0, [b, 'OUT']) # put b on the top
                print("a -> b",a, b)
            
            elif fanout > 1: # Case 2
                print("-----------------------------------------------CASE 2 OUT")
                print("Fanout:", L_fanout[a])
                
                '''
                get_elem = False
                for elem in L_fanout[a]:
                    if elem not in VISITED:
                        Stack.insert(0, [elem, 'OUT'])
                        b = elem            #  # get the elem more in the right
                        get_elem = True
                
                if not get_elem:
                    print("Already visited")
                    continue
                VISITED.append(b)       # PUT b visited
                '''
                b = L_fanout[a][0]  # get the element more left side

                L_fanout[a].remove(b)
                L_fanin[b].remove(a)
                if b not in VISITED: 
                    EDGES.append([a,b,'O'])

                Stack.insert(0, [b, 'OUT']) # put b on the top
                print("a -> b",a, b)
        
        VISITED.append(a)
        #print_grid(grid, GRID_SIZE, len(grid))
        #print("vector pos_x:", pos_x)
        #print("vector pos_y:", pos_y)
        print()
    for i in EDGES:
        print(i)

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
