def count_split_inversions(array):
    """
    Counts the number of split inversions in an array array. 
    An inversion is a pair (i, j) such that i < j and array[i] > array[j].
    array split inversion is one in which i <= n/2 < j
    
    Args:
        array: The array to be analyzed for split inversions.
        
    Returns:
        split_inversions: The total number of split inversions in the array
    """

    def count_split_inversions_helper(array, inversion_count):
        array_length = len(array)

        if array_length == 1:
            return array, inversion_count
        else:
            left_subarray, inversion_count = count_split_inversions_helper(left_side(array), inversion_count)
            right_subarray, inversion_count = count_split_inversions_helper(right_side(array), inversion_count)
            
            sorted_array = []
            i = 0
            j = 0

            for _ in range(array_length):
                if i < len(left_subarray) and j < len(right_subarray):
                    #If the currently-pointed-to element in the left half is smaller than that in the right half, insert it into the sorted array
                    if left_subarray[i] < right_subarray[j]:
                        sorted_array.append(left_subarray[i])
                        i = i + 1
                    else:
                        #Otherwise, put the currently-pointed-to element in the right half into the sorted array
                        sorted_array.append(right_subarray[j])
                        j = j + 1
                        #There are still elements in the left half, and they must be greater than the current element in the right half; i.e. they are inversions.
                        inversion_count += (len(left_subarray) - i)
                elif j >= len(right_subarray):
                    #If the right half has been fully traversed, append the remaining elements from the left half
                    sorted_array.append(left_subarray[i])
                    i = i + 1
                elif i >= len(left_subarray):
                    #If the left half has been fully traversed, append the remaining elements in the right half
                    sorted_array.append(right_subarray[j])
                    j = j + 1
                    
        return sorted_array, inversion_count

    split_inversions = 0
    array, split_inversions = count_split_inversions_helper(array, split_inversions)

    return split_inversions


def left_side(array):
    return array[0:len(array)//2]


def right_side(array):
    return array[len(array)//2:]

if __name__ == '__main__':
    #Read in the text file of integers and store it in a list
    text_file = open('IntegerArray.txt')
    array = []
    for line in text_file:
        array.append(int(line))

    total_inversions = count_split_inversions(array)
    print(total_inversions)