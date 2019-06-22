import math
import multiprocessing as mp
from timeit import default_timer as timer

def two_sum(args):
    test_values, number_list = args
    count = 0
    for t in test_values:
        for y in number_list:
            x = t - y
            if x in hash_table and x != y:
                complements.append((hash_table[x], y))
                count +=1
                print(t,x)
                print(count)
                print('\n')
                break
            
    return count
            
if __name__ == '__main__':
    hash_table = {}
    count = 0
    complements = []
    
    file = open('algo1-programming_prob-2sum.txt')
    for line in file:
        hash_table[int(line)] = int(line)
        
    file = open('algo1-programming_prob-2sum.txt')
    number_list = [int(line) for line in file]
    
    low = -10000
    high = 10001
    n = high - low
    procs = mp.cpu_count()

    sizeSegment = n/procs

    # Create size segments list
    jobs = []
    for i in range(0, procs):
        jobs.append((range(math.ceil(i*sizeSegment-10000), 
                           math.ceil((i+1)*sizeSegment-10000)), number_list))

    start = timer()
    with mp.Pool(procs).map(two_sum, jobs) as pool:
        result = sum(pool)
    duration = timer() - start
    
    print('The number of distinct test values with a two-sum in the provided file is {}'.format(result))
    print('This computation was performed using {0} processes and took {1:0.2f} seconds to complete'.format(procs, duration))