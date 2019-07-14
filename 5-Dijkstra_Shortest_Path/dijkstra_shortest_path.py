def dijkstra(adj_list, source_node):
    """
    Determines the shortest path from the chosen source node to every other node in the graph.
    
    Args:
        adj_list: The adjacency list representation of the graph to be analyzed.
        For some node n with neighboring nodes m1, m2, ... mn whose respective 
        weights are w1, w2, ... wn, the mapping looks like n: {m1:w1, m2:w2, ..., mn:wn}
    Returns:
        List containing the shortest path to each node in the graph. A[i] = shortest path of node i.
    """
    V = list(adj_list.keys())
    X = [source_node]

    # Given graph is 1-indexed but python is 0-indexed. V = {1, 2, ..., n}, so len(V) = n. 
    # Zero is not included in V, so we must initialize n + 1 = len(V) + 1 total elements.
    # Index zero is never used, and the elements of interest are indexed 1 through n inclusive.
    # This is done so that the resultant vertices are indexed the same way as in the problem statement.
    A = [0] * (len(V) + 1) 
    
    while not (set(X) == set(V)):
        greedy_score = float('inf')
        for v in X:
            for w in adj_list[v]:
                if w not in X:
                    old_greedy_score = greedy_score
                    greedy_score = min(greedy_score, A[v] + adj_list[v][w])
                    if not old_greedy_score == greedy_score:
                        w_star = w
        A[w_star] = greedy_score
        X.append(w_star)
            
    return A
        

if __name__ == '__main__':
    # Reads in adjacency list from text file and parses it into a dictionary
    temp_list = []
    file = open('dijkstraData.txt')
    for line in file:
        temp_list.append(line.split())
        
    adj_list = dict((int(row[0]), dict((int(el.split(',')[0]), int(el.split(',')[1])) for el in row[1:])) for row in temp_list)

    # Run Dijkstra's algorithm on the graph represented by adj_list, starting from node 1 (since input graph is 1-indexed)
    A = dijkstra(adj_list, 1)

    # The shortest paths to the nodes requested in the problem statement
    answers = [A[7], A[37], A[59], A[82], A[99], A[115], A[133], A[165], A[188], A[197]]
    print(answers)