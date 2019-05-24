import collections
from Digraph_Class import Digraph


def kosaraju(adj_list):
    #Reverse the graph, first step in Kosaraju's two-pass algorithm
    adj_list_rev = []
    for i in adj_list:
        adj_list_rev.append(i[::-1])

    G_rev = Digraph(adj_list_rev)

    #Run DFS_Loop on the reversed graph to obtain finishing times (second step of Kosaraju's two-pass algorithm)
    DFS_Loop(G_rev)

    #Relabel the nodes of the original graph G so that their number reflects their finishing time from the DFS_Loop call on G_rev
    for i, edge in enumerate(adj_list):
        for j, node in enumerate(edge):
            adj_list[i][j] = G_rev.finishing_time[node]

    G = Digraph(adj_list)

    #Run DFS_Loop on the relabeled graph to obtain leaders (third step in Kosaraju's two-step algorithm)
    DFS_Loop(G)
        
    leader = []
    for value in G.leader.values():
        leader.append(value)
        
    #Counts how many times each leader appears (recall all nodes with the same leader form an SCC)
    SCCs = collections.Counter(leader)
    vals = list(SCCs.values())

    return vals


def DFS_Loop(G):
    """
    Loops through nodes in descending order, calling DFS on any that have not been explored yet.
    
    Args:
        G: The directed graph to be searched.
    """
    global finishing_time
    global DFS_call_node
    
    finishing_time = 0
    DFS_call_node = None
    
    for node in range(G.n, 0, -1):
        if not G.explored[node]:
            #Keep track of which node DFS was called from, so that the leader dictionary can use this information
            DFS_call_node = node
            DFS(G, node)
           

def DFS(G, source_node):
    """
    Initiates a depth first search on the graph G starting with the specified source node.
    
    Args:
        G: A graph of type Digraph
        source_node: The node that depth first search is to begin on
    """
    global finishing_time
    global DFS_call_node
    
    #List which will be used to keep track of which nodes were explored and in what order
    order_explored = []
    
    G.mark_explored(source_node)
    G.set_leader(source_node, DFS_call_node)
    order_explored.append(source_node)
    
    #A list of all the head nodes pointed to by the source node
    nodes_to_visit = G.edges[source_node]
    
    #The nodes_to_visit list is treated as a stack. Every time a node is explored, it is popped off the stack. 
    #Any head nodes pointed to by the just-explored node are pushed onto the stack, so that they are explored first (i.e. depth first).
    while nodes_to_visit:
        head_node = nodes_to_visit.pop()
        if not G.explored[head_node]:
            G.mark_explored(head_node)
            G.set_leader(head_node, DFS_call_node)
            order_explored.append(head_node)
            
            nodes_to_visit.extend(G.edges[head_node])
    
    #Order explored is also treated as a stack. It contains all the nodes explored by this call of DFS in order of finishing time.
    while order_explored:
        node = order_explored.pop()
        finishing_time = finishing_time + 1
        G.set_finishing_time(node,finishing_time)


if __name__ == '__main__':
    file = open('SCC.txt')
    adj_list = []
    for line in file:
        adj_list.append([int(x) for x in line.split()])
    
    SCC_sizes = kosaraju(adj_list)

    sorted_SCC_sizes = sorted(SCC_sizes, reverse=True)

    #The sizes of the five largest SCCs
    top_five = sorted_SCC_sizes[0:5]