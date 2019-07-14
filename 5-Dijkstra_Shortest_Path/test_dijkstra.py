import pytest
from dijkstra_shortest_path import dijkstra

# Adjacency list of example graph from lectures
adj_list = {
        1: {2:1, 3:4},
        2: {3:2, 4:6},
        3: {4:3},
        4: {}
        }
source_node = 1
expected = [0, 0, 1, 3, 6]
t1 = (adj_list, source_node, expected)

# Reads in adjacency list from text file and parses it into a dictionary
temp_list = []
file = open('dijkstraData.txt')
for line in file:
    temp_list.append(line.split())
    
adj_list = dict((int(row[0]), dict((int(el.split(',')[0]), int(el.split(',')[1])) for el in row[1:])) for row in temp_list)

source_node = 1
expected = \
[0, 0, 2971, 2644, 3056, 2525, 2818, 2599, 1875, 745, 3205, 1551, 2906, 2394, 1803, 2942, 1837, 3111, 2284, 1044, 
2351, 3630, 4028, 2650, 3653, 2249, 2150, 1222, 2090, 3540, 2303, 3455, 3004, 2551, 2656, 998, 2236, 2610, 3548, 
1851, 4091, 2732, 2040, 3312, 2142, 3438, 2937, 2979, 2757, 2437, 3152, 2503, 2817, 2420, 3369, 2862, 2609, 2857, 
3668, 2947, 2592, 1676, 2573, 2498, 2047, 826, 3393, 2535, 4636, 3650, 743, 1265, 1539, 3007, 4286, 2720, 3220, 
2298, 2795, 2806, 982, 2976, 2052, 3997, 2656, 1193, 2461, 1608, 3046, 3261, 2018, 2786, 647, 3542, 3415, 2186, 
2398, 4248, 3515, 2367, 2970, 3536, 2478, 1826, 2551, 3368, 2303, 2540, 1169, 3140, 2317, 2535, 1759, 1899, 508, 
2399, 3513, 2597, 2176, 1090, 2328, 2818, 1306, 2805, 2057, 2618, 1694, 3285, 1203, 676, 1820, 1445, 2468, 2029, 
1257, 1533, 2417, 3599, 2494, 4101, 546, 1889, 2616, 2141, 2359, 648, 2682, 3464, 2873, 3109, 2183, 4159, 1832, 
2080, 1831, 2001, 3013, 2143, 1376, 1627, 2403, 4772, 2556, 2124, 1693, 2442, 3814, 2630, 2038, 2776, 1365, 3929,
1990, 2069, 3558, 1432, 2279, 3829, 2435, 3691, 3027, 2345, 3807, 2145, 2703, 2884, 3806, 1151, 2505, 2340, 2596,
4123, 1737, 3136, 1073, 1707, 2417, 3068, 1724, 815, 2060]

t2 = (adj_list, source_node, expected)

test_cases = [t1, t2]

@pytest.mark.parametrize('adj_list, source_node, expected', test_cases)
def test_dijkstra(adj_list, source_node, expected):
    actual = dijkstra(adj_list, source_node)

    assert(expected == actual)