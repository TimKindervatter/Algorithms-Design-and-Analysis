import collections

class Digraph:
    """
    A class defining a directed graph object.
    """
    def __init__(self, adj_list):
        """
        Constructor for the Digraph class.
        
        Args:
            adj_list: The adjacency list representation of the directed graph.
                Adjacency list must be a list of lists, where each sublist represents one edge. 
                Each sublist has two elements; the first element is the tail node, and the second element is the head node.
        """
        
        #Obtains a set (i.e. no repeats) of all the nodes in the digraph
        all_nodes = []
        for i in adj_list:
            all_nodes.append(i[0])
            all_nodes.append(i[1])
        unique_nodes = set(all_nodes)
        
        #Number of nodes in the graph
        self.n = len(unique_nodes)
        
        #Uses adj_list to create a dictionary whose keys are tail nodes and 
        #whose values are lists of all the head nodes pointing to that tail node
        self.edges = dict((el+1,[]) for el in range(self.n))
        for edge in adj_list:
            tail_node = int(edge[0])
            head_node = int(edge[1])
            self.edges[tail_node].append(head_node)
        
        #Initializes an empty dictionary whose keys are nodes and whose value
        #denotes whether it has been explored (True) or not (False)
        self.explored = dict((el+1, False) for el in range(self.n))
        
        #Initializes an empty dictionary whose keys are nodes and whose value
        #denotes which node DFS was called on to explore this node
        self.leader = dict((el+1, None) for el in range(self.n))
        
        #Initializes an empty dictionary whose keys are nodes and whose value
        #denotes the finishing time of the node
        self.finishing_time = dict((el+1, None) for el in range(self.n))
        
    def mark_explored(self, explored_node):
        """
        Uses the input node as the key and changes the corresponding value of 
        the explored dictionary to True.
        
        Args:
            explored_node: The number of the node to be marked as explored
        """
        self.explored[explored_node] = True
        
    def set_finishing_time(self, explored_node, finishing_time):
        """
        Uses the input node as the key and changes the corresponding value of 
        the finishing time dictionary to the running count of finishing time.
        
        Args:
            explored_node: The node whose finishing time is to be specified.
            finishing_time: The running count of the number of nodes explored so far.
        """
        self.finishing_time[explored_node] = finishing_time
        
    def set_leader(self, explored_node, DFS_call_node):
        """
        Uses the input node as the key and changes the corresponding value of 
        the leader dictionary to the node that DFS was called on.
        
        Args:
            explored_node: The node that was just explored and whose leader is to be specified.
            DFS_call_node: The node that the current DFS call originated from.
        """
        self.leader[explored_node] = DFS_call_node

def DFS(G,source_node):
    """
    Initiates a depth first search on the graph G starting with the specified source node.
    
    Args:
        G: A graph of type Digraph
        source_node: The node that depth first search is to begin on
    """
    global finishing_time
    global DFS_call_node
    
    #List which will be used to keep track of which nodes were explored
    #and in what order
    order_explored = []
    
    #Mark the source node as explored, make a note of its leader, and append it
    #to the list of explored nodes
    G.mark_explored(source_node)
    G.set_leader(source_node, DFS_call_node)
    order_explored.append(source_node)
    
    #A list of all the head nodes pointed to by the source node
    nodes_to_visit = G.edges[source_node]
    
    #In the lecture, DFS was implemented recursively. However, the recursion depth
    #required to solve the problem is greater than python's recursion limit. I 
    #rewrote the code to use a stack instead of recursive calls on DFS.
    
    #The nodes_to_visit list is treated as a stack. Every time a node is explored,
    #it is popped off the stack. Any head nodes pointed to by the just-explored
    #node are pushed onto the stack, so that they are explored first (i.e. depth first)
    while nodes_to_visit:
        #Pop the next node to be explored off of the stack
        head_node = nodes_to_visit.pop()
        #As long as the node popped off the stack hasn't been explored yet...
        if not G.explored[head_node]:
            #Mark it as explored, make a note of its leader, and append it to
            #the list of explored nodes
            G.mark_explored(head_node)
            G.set_leader(head_node, DFS_call_node)
            order_explored.append(head_node)
            
            #Push any nodes pointed to by the just-explored node onto the stack
            nodes_to_visit.extend(G.edges[head_node])
    
    #Order explored is also treated as a stack. It contains all the nodes explored
    #by this call of DFS in order of finishing time.
    while order_explored:
        #Nodes are popped off the stack one-by-one
        node = order_explored.pop()
        #They are assigned a finishing time according to the running total
        finishing_time = finishing_time + 1
        G.set_finishing_time(node,finishing_time)
    
def DFS_Loop(G):
    """
    Loops through nodes in descending order, calling DFS on any that have not been explored yet.\
    
    Args:
        G: The directed graph to be searched.
    """
    global finishing_time
    global DFS_call_node
    
    finishing_time = 0
    DFS_call_node = None
    
    #Loop through each node in descending order
    for node in range(G.n, 0, -1):
        #If the node hasn't been explored yet, call DFS on it
        if not G.explored[node]:
            #Keep track of which node DFS was called from, so that the leader 
            #dictionary can use this information
            DFS_call_node = node
            DFS(G, node)
           
            
#Allows toggling of simple example array from lectures for easy debugging
test_case = False

if test_case:
    #Reversed graph given as an example in the lectures
    adj_list_rev = [[1,7], [2,5], [3,9], [4,1], [5,8], [6,3], [6,8], [7,4], [7,9], [8,2], [9,6]]
    
    #Reverse the graph
    adj_list = []
    for i in adj_list_rev:
        adj_list.append(i[::-1])
else:
    #Read in the adjacency list from the provided text file
    file = open('SCC.txt')
    adj_list = []
    for line in file:
        adj_list.append([int(x) for x in line.split()])
    
    #Reverse the graph, first step in Kosaraju's two-pass algorithm
    adj_list_rev = []
    for i in adj_list:
        adj_list_rev.append(i[::-1])

#Create a Digraph object for the reversed graph
G_rev = Digraph(adj_list_rev)
#Run DFS_Loop on the reversed graph to obtain finishing times (second step of
#Kosaraju's two-pass algorithm)
DFS_Loop(G_rev)

#Relabel the nodes of the original graph G so that their number reflects their
#finishing time from the DFS_Loop call on G_rev
for i, edge in enumerate(adj_list):
    for j, node in enumerate(edge):
        adj_list[i][j] = G_rev.finishing_time[node]

#Create a Digraph object out of the relabeled graph
G = Digraph(adj_list)
#Run DFS_Loop on the relabeled graph to obtain leaders (third step in Kosaraju's
#two-step algorithm)
DFS_Loop(G)
    
#Create a list containing the leaders of each node in G
leader = []
for value in G.leader.values():
    leader.append(value)
    
#Counts how many times each leader appears (recall all nodes with the same
#leader form an SCC)
SCCs = collections.Counter(leader)
vals = list(SCCs.values())

#Sorts the number of leader occurrences in descending order so that we can identify
#the five largest SCCs
sorted_vals = sorted(vals, reverse=True)

#The sizes of the five largest SCCs
top_five = sorted_vals[0:5]