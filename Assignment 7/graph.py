from operator import itemgetter


class Graph:
    """
    A class defining a graph object.
    """

    tail_nodes = []
    head_nodes = []

    def __init__(self, adj_list):
        """
        Constructor for the Graph class.

        Args:
            adj_list: The adjacency list representation of the graph. Adjacency list must be a list of lists,
            where each sublist represents one edge. Each sublist has two elements;
            the first element is the tail node, and the second element is the head node.
        """

        self.tail_nodes = self.read_tail_nodes(adj_list)
        self.head_nodes = self.read_head_nodes(adj_list)

        self.n = self.compute_number_of_nodes(adj_list)

        self.edges = self.create_edges(adj_list)
        # Keys are nodes and values denote whether that node has been explored (True) or not (False)
        self.explored = dict((el+1, False) for el in range(self.n))

    def read_tail_nodes(self, adj_list):
        return list(map(itemgetter(0), adj_list))

    def read_head_nodes(self, adj_list):
        return list(map(itemgetter(1), adj_list))

    def compute_number_of_nodes(self, adj_list):
        # Obtains a set (i.e. no repeats) of all the nodes in the digraph
        all_nodes = []
        all_nodes += self.tail_nodes
        all_nodes += self.head_nodes
        unique_nodes = set(all_nodes)

        # Number of nodes in the graph
        return len(unique_nodes)

    def create_edges(self, adj_list):
        # Keys are tail nodes and values are lists of all the head nodes associated with that tail node
        edges = dict((el+1, []) for el in range(self.n))
        for edge in adj_list:
            tail_node = int(edge[0])
            head_node = int(edge[1])
            edges[tail_node].append(head_node)

        return edges

    def mark_explored(self, explored_node):
        """
        Uses the input node as the key and changes the corresponding value of the explored dictionary to True.

        Args:
            explored_node: The number of the node to be marked as explored
        """
        self.explored[explored_node] = True


class Digraph(Graph):
    """
    A class defining a directed graph object.
    """
    def __init__(self, adj_list):
        """
        Constructor for the Digraph class.

        Args:
            adj_list: The adjacency list representation of the directed graph. Adjacency list must be a list of lists,
                where each sublist represents one edge. Each sublist has two elements;
                the first element is the tail node, and the second element is the head node.
        """

        super().__init__(adj_list)

        # Keys are nodes and values denote which node DFS was called on to explore that node
        self.leader = dict((el+1, None) for el in range(self.n))

        # Keys are nodes and values are the finishing times of each node
        self.finishing_time = dict((el+1, None) for el in range(self.n))

    def set_finishing_time(self, explored_node, finishing_time):
        """
        Uses the input node as the key and changes the corresponding value of the finishing time dictionary to the
        running count of finishing time.

        Args:
            explored_node: The node whose finishing time is to be specified.
            finishing_time: The running count of the number of nodes explored so far.
        """
        self.finishing_time[explored_node] = finishing_time

    def set_leader(self, explored_node, DFS_call_node):
        """
        Uses the input node as the key and changes the corresponding value of the leader dictionary to the
        node that DFS was called on.

        Args:
            explored_node: The node that was just explored and whose leader is to be specified.
            DFS_call_node: The node that the current DFS call originated from.
        """
        self.leader[explored_node] = DFS_call_node


class Weighted_Graph(Graph):

    def __init__(self, adj_list):
        super().__init__(adj_list)

    def create_edges(self, adj_list):
        # Keys are tail nodes and values are lists of all the head nodes associated with that tail node
        edges = dict((el+1, []) for el in range(self.n))
        for edge in adj_list:
            tail_node = int(edge[0])
            head_node = int(edge[1])
            edge_weight = int(edge[2])

            weighted_edge = {(tail_node, head_node): edge_weight}

            edges[tail_node].append(weighted_edge)

        return edges

"""         self.edge_weights = self.read_edge_weights(adj_list)



    def read_edge_weights(self, adj_list):
        return list(map(itemgetter(2), adj_list)) """

