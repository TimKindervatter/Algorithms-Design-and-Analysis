import heapq

file = open('Median.txt')

file_contents = []
running_sum = 0

for line in file:
    file_contents.append(int(line))
    
lower = min(file_contents[0], file_contents[1])
higher = max(file_contents[0], file_contents[1])

H_high = [higher]
H_low = [-lower]

medians = []

medians.append(higher)
medians.append(lower)

heapq.heapify(H_low)
heapq.heapify(H_high)

for el in file_contents[2:]:
    lower = H_low[-1]
    higher = H_high[0]
    
    if el < lower:
        heapq.heappush(H_low, el)
    elif el > lower and el < higher:
        heapq.heappush(H_low, -el)
    elif el > higher:
        heapq.heappush(H_high, el)     
    
    if len(H_low) - len(H_high) > 1:
        temp = -heapq.heappop(H_low)
        heapq.heappush(H_high, temp)
    if len(H_high) - len(H_low) > 1:
        temp = -heapq.heappop(H_high)
        heapq.heappush(H_low, temp)
        
    if len(H_low) == len(H_high):
        median = -H_low[0]
    if len(H_low) > len(H_high):
        median = -H_low[0]
    if len(H_low) < len(H_high):
        median = H_high[0]
    
    medians.append(median)
    
answer = sum(medians) % 10000