def count_split_inversions(A):
    """
    Counts the number of split inversions in an array A. 
    An inversion is a pair (i, j) such that i < j and A[i] > A[j].
    A split inversion is one in which i <= n/2 < j
    
    Args:
        A: The array to be analyzed for split inversions.
        
    Returns:
        A sorted version of A (this algorithm for counting split inversions piggybacks on merge sort).
    """

    def count_split_inversions_helper(A, inversion_count):
        n = len(A)
        
        if n == 1:
            return A, inversion_count
        else:
            B, inversion_count = count_split_inversions_helper(A[0:n//2], inversion_count)
            C, inversion_count = count_split_inversions_helper(A[n//2:], inversion_count)
            
            D = []
            i = 0
            j = 0

            for k in range(n):
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
                        #element in the right half; i.e. they are inversions.
                        inversion_count += (len(B) - i)
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
        return D, inversion_count

    split_inversions = 0
    A, split_inversions = count_split_inversions_helper(A, split_inversions)

    return split_inversions

if __name__ == '__main__':
    #Read in the text file of integers and store it in a list
    text_file = open('IntegerArray.txt')
    A = []
    for line in text_file:
        A.append(int(line))

    split_inversions = 0 #Initialize split_inversions
    total_inversions = count_split_inversions(A)
    print(total_inversions)