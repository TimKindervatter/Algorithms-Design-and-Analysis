hash_table = {}
count = 0
complements = []


file = open('algo1-programming_prob-2sum.txt')
for line in file:
    hash_table[int(line)] = int(line)
    
file = open('algo1-programming_prob-2sum.txt')
number_list = [int(line) for line in file]
    
#for i in range(10):
#    hash_table[i] = i


count = 0
for t in range(-10000, 10001):
    for y in number_list:
        x = t - y
        if x in hash_table and x != y:
            complements.append((hash_table[x], y))
            count +=1
            print(t,x)
            print(count)
            print('\n')
            break