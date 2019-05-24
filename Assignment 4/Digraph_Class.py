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