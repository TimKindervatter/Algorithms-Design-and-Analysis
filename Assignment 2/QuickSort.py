import math
import statistics

#Decided to use global because passing this variable as an argument adds
#unnecessary complexity to such a simple script. Making it global made the code
#much cleaner and more readable.
global number_of_comparisons

def partition(A, l = 0, r = None):
    """
    Partitions an array using its first element as the pivot.
    
    Args:
        A: The array to be partitioned.
        l: The leftmost index of A to consider (becomes the pivot p).
            Defaults to the first element of A.
        r: The rightmost index of A to consider. 
            Defaults to the last element of A.
    Returns:
        Array whose elements to the left of the pivot p are all <p, and whose 
        elements to the right of p are all >p. Elements are not guaranteed to 
        be sorted.
    """
    
    global number_of_comparisons
    
    #Default value for r is the length of the input array
    if r is None:
        r = len(A)
    
    #The number of comparisons performed is the number of elements considered
    #for partitioning (r-l), minus the pivot
    number_of_comparisons = number_of_comparisons + ((r-l) - 1)
    
    #Chooses the first element of the array as the pivot
    p = A[l]
    #Index i divides the already partitioned elements into <p and >p
    #i is initialized immediately to the right of p
    i = l + 1
    #Index j separates partitioned elements from unpartitioned ones
    #Increment j along all elements after the pivot - i.e. from the element 
    #immediately to the right of p all the way up to r
    for j in range(l+1,r):
        #If the next unpartitioned element is smaller than the pivot...
        if A[j] < p:
            #Swap the ith and jth elements of A
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            #Increment i to indicate that the recently swapped element belongs
            #to the <p partition
            i = i + 1
    #Once all elements have been partitioned, swap the first element (the pivot)
    #with the element immediately before i
    temp = A[i - 1]
    A[i - 1] = A[l]
    A[l] = temp
    
    #Return the partitioned array [<p, p, >p]
    return [A[0:i-1], [p], A[i:]]


def quicksort(A, pivot_strategy = 1):
    """
    Sorts the elements of the array A in ascending order.
    
    Args:
        A: The array to be sorted.
        pivot_strategy: The strategy employed for choosing a pivot element.
            An input value of 1 chooses the first element. 
            An input value of 2 chooses the last element. 
            An input value of 3 chooses the median of the first, middle, and last elements.
    Returns:
        An array containing the elements of the input array, sorted in ascending order.
    """
    
    if pivot_strategy < 1 or pivot_strategy > 3:
        raise ValueError('pivot_strategy must equal 1, 2, or 3. The value provided was: {}'.format(pivot_strategy))
    
    #Recursion base case
    if len(A) == 1:
        return A
    else:
        #Question 2 asks to choose the last element of A as the pivot, rather
        #than the first. This preprocessing step swaps the first and last elements
        #of A, accomplishing this goal.
        if pivot_strategy == 2:
            temp = A[0]
            A[0] = A[-1]
            A[-1] = temp
        #Question 3 asks to choose the median of the first, middle, and last 
        #elements of A as the pivot, rather than the first.
        elif pivot_strategy == 3:
            #Identifies the first, middle, and last elements of A
            first = A[0]
            middle = A[math.ceil(len(A)/2)-1]
            last = A[-1]
            
            #Computes the median of these three elements and finds its index in A
            median_of_three = statistics.median([first, middle, last])
            median_of_three_index = A.index(median_of_three)
            
            #Swaps the first element of A with the median of three element
            temp = A[0]
            A[0] = A[median_of_three_index]
            A[median_of_three_index] = temp
        
        #Partitions A to receive an array [<p, p, >p]
        partitioned_array = partition(A)
        
        lp = partitioned_array[0] #The subarray <p
        p = partitioned_array[1]  #The pivot p
        gp = partitioned_array[2] #The subarray >p
        
        #As long as there are elements in the subarray <p, recursively call
        #quicksort to sort this smaller problem
        if len(lp) > 0:
            lp = quicksort(lp, pivot_strategy)
        #As long as there are elements in the subarray <p, recursively call
        #quicksort to sort this smaller problem
        if len(gp) > 0:
            gp = quicksort(gp, pivot_strategy)
            
        #At the end of all the recursive calls, <p and >p will now be sorted
        #Concatenate <p, p, and >p to obtain a sorted version of the original
        #array A
        A = lp + p + gp
        return A


#Allows toggling of simple example array from lectures for easy debugging
test_case = False

if test_case:
    #Example array from lectures
    A = [3,8,2,5,1,4,7,6]
else:
    #Read the text file into an array A
    text_file = open('QuickSort_Array.txt')
    A = []
    for line in text_file:
        A.append(int(line))

number_of_comparisons = 0
#Simple switch between pivot choice strategy for problems 1, 2, and 3
pivot_strategy = 1
A = quicksort(A, pivot_strategy)