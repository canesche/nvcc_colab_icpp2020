import sys
import networkx as nx
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

    #for no in dic_id:
    #    print(dic_id[no], no)

    return dic_id, count, len(EDGE)

def dfs_zigzag(g, LIST, VISITED, NEW_EDGE, left):
    
    while len(LIST) > 0:
        if left:
            node, direction = LIST.pop(0) # remove stack
        else:
            node, direction = LIST.pop()
        #print("LIST = ", LIST)
        #print(node, direction)
        #input()

        if direction == 'IN':
            for n in list(g.predecessors(node)):
                if n not in VISITED:
                    NEW_EDGE.append([n, node])
                    #print("%s -> %s %s" %(n, node, direction))
                    VISITED.append(n)
                    LIST.insert(0, [n, 'IN']) # simulated recursive
                    if g.out_degree(n) > 1:
                        #if g.out_degree(n) > 1:
                        #    LIST.insert(0, [node, 'IN'])
                        LIST.insert(0, [n, 'OUT']) # change to other direction
                        #print("inverte direcao para OUT")
                        break
                    if g.in_degree(n) > 1:
                        LIST.insert(0, [node, 'IN'])
                        #print("adiciona %s IN" % n)
                    
        else: # direction OUT
            for n in list(g.successors(node)):
                if n not in VISITED:
                    NEW_EDGE.append([node, n])
                    #print("%s -> %s %s" %(node, n, direction))
                    VISITED.append(n)
                    LIST.insert(0, [n, 'OUT']) # simulated recursive
                    if g.in_degree(n) > 1:
                        #if g.out_degree(n) > 1:
                        #    LIST.insert(0, [node, 'OUT'])
                        LIST.insert(0, [n, 'IN']) # change to other direction
                        #print("inverte direcao para IN")
                        break
                    if g.out_degree(n) > 1:
                        LIST.insert(0, [n, 'OUT'])
                        #print("adiciona %s OUT" % n)
        

def create_list_zigzag(g, dic_id, EDGE, N_NODE):

    OUTS = []
    # get the node inputs
    for n in g.nodes():
        if g.out_degree(n) == 0:
            OUTS.append(n)
    
    #print(OUTS)
    for k in range(len(OUTS)):
        OUTS[0], OUTS[k] = OUTS[k], OUTS[0]
        for j in range(2):
            NEW_EDGE = []
            EDGE_LIST = []
            LIST = []
            VISITED = []
            if (j % 2 == 0):
                left = True
            else:
                left = False
            for no in OUTS:
                if no not in VISITED:
                    VISITED.append(no)
                    LIST.insert(0, [no, 'IN']) # insert stack
                    dfs_zigzag(g, LIST, VISITED, NEW_EDGE, left)

            for i in range(len(EDGE)):
                if EDGE[i] not in NEW_EDGE:
                    NEW_EDGE.append(EDGE[i])
            
                EDGE_LIST.append(str(dic_id[NEW_EDGE[i][0]]))
                EDGE_LIST.append(str(dic_id[NEW_EDGE[i][1]]))

            for i in range(0,len(EDGE_LIST),2):
                print(EDGE_LIST[i]+" "+EDGE_LIST[i+1]+" ", end="")
            print("\n")

            for i in range(len(EDGE_LIST)-1,0,-2):
                print(EDGE_LIST[i-1]+" "+EDGE_LIST[i]+" ", end="")
            print("\n")

def create_list_zigzag_single(g, dic_id, EDGE, N_NODE):

    OUTS = []
    # get the node inputs
    for n in g.nodes():
        if g.out_degree(n) == 0:
            OUTS.append(n)
    
    NEW_EDGE = []
    EDGE_LIST = []
    LIST = []
    VISITED = []
    
    for no in OUTS:
        if no not in VISITED:
            VISITED.append(no)
            LIST.insert(0, [no, 'IN']) # insert stack
            dfs_zigzag(g, LIST, VISITED, NEW_EDGE, True)

    for i in range(len(EDGE)):
        if EDGE[i] not in NEW_EDGE:
            NEW_EDGE.append(EDGE[i])
    
        EDGE_LIST.append(str(dic_id[NEW_EDGE[i][0]]))
        EDGE_LIST.append(str(dic_id[NEW_EDGE[i][1]]))

    for i in range(0,len(EDGE_LIST),2):
        print(EDGE_LIST[i]+" "+EDGE_LIST[i+1]+" ", end="")
    print("\n")

def create_list_largura(g, dic_id):

    EDGE_LIST = []
    OPEN = []
    for n in g.nodes():
        if g.in_degree(n) == 0:
            OPEN.insert(0,n)

    CLOSED = []
    while len(OPEN) > 0 :
        node = OPEN.pop()
        CLOSED.append(node)
        for no in list(g.successors(node)):
            EDGE_LIST.append(str(dic_id[node]))
            EDGE_LIST.append(str(dic_id[no]))
            if no not in OPEN and no not in CLOSED:
                OPEN.insert(0, no)

    for i in range(0,len(EDGE_LIST),2):
        print(EDGE_LIST[i]+" "+EDGE_LIST[i+1]+" ", end="")
    print("\n")

    for i in range(len(EDGE_LIST)-1,0,-2):
        print(EDGE_LIST[i-1]+" "+EDGE_LIST[i]+" ", end="")
    print("\n")
        
def create_list_profundidade(g, dic_id):
    
    EDGE_LIST = []
    OPEN = []
    for n in g.nodes():
        if g.in_degree(n) == 0:
            OPEN.append(n)

    CLOSED = []
    while len(OPEN) > 0 :
        node = OPEN.pop(0)
        CLOSED.append(node)
        for no in list(g.successors(node)):
            EDGE_LIST.append(str(dic_id[node]))
            EDGE_LIST.append(str(dic_id[no]))
            if no not in OPEN and no not in CLOSED:
                OPEN.insert(0, no)
    
    for i in range(0,len(EDGE_LIST),2):
        print(EDGE_LIST[i]+" "+EDGE_LIST[i+1]+" ", end="")
    print("\n")

    #for i in range(len(EDGE_LIST)-1,0,-2):
    #    print(EDGE_LIST[i-1]+" "+EDGE_LIST[i]+" ", end="")
    #print("\n")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        dot = sys.argv[1]
    else:
        print("python3 dot_to_list <name.dot>\n")
        exit(0)
    
    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    EDGE = []
    dic_id, N_NODE, N_EDGE = create_id(g, EDGE)

    for node in dic_id:
        print(dic_id[node], node)

    #print(str(N_NODE) + " " + str(N_EDGE) + "\n")

    #create_list_zigzag_single(g, dic_id, EDGE, N_NODE)

    #create_list_zigzag(g, dic_id, EDGE, N_NODE)

    #create_list_largura(g, dic_id)

    #create_list_profundidade(g, dic_id)
