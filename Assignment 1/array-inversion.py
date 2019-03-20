#Decided to use global because passing this variable as an argument adds
#unnecessary complexity to such a simple script. Making it global made the code
#much cleaner and more readable.
global split_inversions

def countSplitInversions(A):
    """
    Counts the number of split inversions in an array A. 
    An inversion is a pair (i, j) such that i < j and A[i] > A[j].
    A split inversion is one in which i <= n/2 < j
    
    Args:
        A: The array to be analyzed for split inversions.
        
    Returns:
        A sorted version of A (this algorithm for counting split inversions piggybacks on merge sort).
    """
    
    global split_inversions
    
    n = len(A)
    
    if n == 1:
        #Recursion base case
        return A
    else:
        #Splits the array A into left and right halves and recursively counts split inversions
        
        #Recursively call countSplitInversions on the first half, 
        #i.e. first n//2 elements, of A
        B = countSplitInversions(A[0:n//2])
        
        #Recursively call countSplitInversions on the second half, 
        #i.e. i.e. elements n//2 to the end, of A
        C = countSplitInversions(A[n//2:])
        
        #Initializes an array D and indices i and j which will be used for the
        #merging step of merge sort
        D = []

        i = 0
        j = 0

        #Increments along the left and right halves of A in parallel
        #The first element in each array is compared, the smaller of the two 
        #is placed in D, and the array that contained the smaller element has 
        #its index incremented
        for k in range(n):
            #If neither array has been fully traversed, compare the current 
            #elements pointed to in both halves
            if i < len(B) and j < len(C):
                #If the currently-pointed-to element in the left half is 
                #smaller than that in the right half, insert it into D
                if B[i] < C[j]:
                    D.append(B[i])
                    i = i + 1
                else:
                    #Otherwise, put the currently-pointed-to element in the right half in D
                    D.append(C[j])
                    j = j + 1
                    #There are still elements in the left half, and they must be greater than the current
                    #element in the right half. I.e. they are inversions.
                    #However many elements remain in the left half, add that many inversions to the running total
                    split_inversions = split_inversions + (len(B) - i)
            elif j >= len(C):
                #If the right half has been fully traversed, simply append the remaining elements from the left half
                D.append(B[i])
                i = i + 1
            elif i >= len(B):
                #If the left half has been fully traversed, simply append the remaining elements in the right half
                D.append(C[j])
                j = j + 1
                
    #Return the merge-sorted sublist D for further recursive merges
    #Also return the running total of split inversions for any future recursive calls to take into account
    return D


#Allows toggling of simple example array from lectures for easy debugging
test_case = False

if test_case:
    #Example array from lectures
    A = [1,3,5,2,4,6]
else:
    #Read in the text file of integers and store it in a list
    text_file = open('IntegerArray.txt')
    A = []
    for line in text_file:
        A.append(int(line))

split_inversions = 0 #Initialize split_inversions
total_inversions = countSplitInversions(A)