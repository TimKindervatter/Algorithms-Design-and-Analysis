import random
import math

def contract_node(adj_list):
    """
    Randomly chooses two nodes from the input adjacency list and merges them.
    Parallel edges remain intact.
    
    Args:
        adj_list: Adjacency list representation of an undirected graph. Must be supplied as a list of lists.
    Returns:
        An adjacency list containing one fewer node than the input adjacency list.
    """
    #Randomly choose a row to pick an edge from
    node_to_contract = random.choice(adj_list)[0]
    
    #Store the index of the row
    for i in adj_list:
        if i[0] == node_to_contract:
            contracted_index = adj_list.index(i)
    
    #Randomly pick an adjacent node from within the randomly chosen row
    node_to_survive = random.choice(adj_list[contracted_index][1:])
    
    #Store the index of the row starting with the chosen adjacent node
    for i in adj_list:
        if i[0] == node_to_survive:
            surviving_index = adj_list.index(i)
    
    #Append adjacency list for contracted node onto adjacency list of surviving node
    adj_list[surviving_index] = adj_list[surviving_index] + adj_list[contracted_index][1:]
    adj_list[surviving_index].remove(node_to_contract)
    contracted_node = adj_list[surviving_index][1:]
    
    #Remove all instances of contracted node from surviving node's adjacency list
    for el in contracted_node:
        if el == node_to_survive:
            contracted_node.remove(el)
            
    #Append pruned adjacency list to surviving node's adjacency list
    adj_list[surviving_index] = [node_to_survive] + contracted_node
    
    #Remove the contracted node's adjacency list
    del adj_list[contracted_index]
    
    #Replace all instances of contracted node with that of surviving node
    for i, node in enumerate(adj_list):
        for j, adjacent_node in enumerate(node):
            if adjacent_node == node_to_contract:
                adj_list[i][j] = node_to_survive
                
    return adj_list


#Allows toggling of simple example array from lectures for easy debugging
test_case = False

if test_case:
    init_adj_list = [[1, 2, 3], [2, 1, 3, 4], [3, 1, 2, 4], [4, 2, 3]]
else:
    file= open('C:\\Python\\Stanford Algorithms Problem Sets\\kargerMinCut.txt')
    data = []
    for line in file:
        data.append(line.rstrip().split('\t'))
        
    init_adj_list = [[int(j) for j in i] for i in data]

#Number of nodes in the undirected graph
n = len(init_adj_list)

#This algorithm is random, so it is not guaranteed to give the correct answer on
#any given run. We must run it many times and keep track of the lowest minimum
#cut seen so far.

#As proven in the lecture, running the algorithm n^2ln(n) times gives a 1/n
#chance of getting the correct answer
N = round(n**2*math.log(n,math.e))

#Initialize min_cut to infinity, so that the value calculated by the algorithm
#is necessarily smaller
min_cut = float('inf')

for iteration in range(N):
    adj_list = init_adj_list
    #Continue contracting nodes until there are only 2 left
    while len(adj_list) > 2:
        adj_list = contract_node(adj_list)
        
        #Remove self_loops
        for i,node in enumerate(adj_list):
            adjacent_nodes = node[1:]
            self_loop = adj_list[i][0]
            continue_flag = True
            while continue_flag:
                if self_loop in adjacent_nodes:
                    adjacent_nodes.remove(self_loop)
                else:
                    continue_flag = False
            adj_list[i] = [node[0]] + adjacent_nodes
        
    #Compare the minimum cut calculated on this run with the previous minimum cut
    #found. If the new value from this run is smaller than the previous value, 
    #replace the old one.
    min_cut = min(min_cut, len(adj_list[0])-1)