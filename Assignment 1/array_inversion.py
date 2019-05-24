from pathlib import Path

def count_inversions(array):
    """
    Counts the number of split inversions in an array array. 
    An inversion is a pair (i, j) such that i < j and array[i] > array[j].
    array split inversion is one in which i <= n/2 < j
    
    Args:
        array: The array to be analyzed for split inversions.
        
    Returns:
        inversion_count: The total number of inversions in the array
    """

    array, inversion_count = merge_sort(array)

    return inversion_count


def merge_sort(array):
    array_length = len(array)

    if array_length == 1:
        #Arrays of length 1 cannot have inversions
        total_inversions = 0
        return array, total_inversions
    else:
        left_subarray, left_inversions = merge_sort(get_left_half(array))
        right_subarray, right_inversions = merge_sort(get_right_half(array))
        
        sorted_array, split_inversions = merge_subarrays(left_subarray, right_subarray)

    total_inversions = left_inversions + right_inversions + split_inversions
                
    return sorted_array, total_inversions


def get_left_half(array):
    return array[0:len(array)//2]


def get_right_half(array):
    return array[len(array)//2:]
    

def merge_subarrays(left_subarray, right_subarray):
    sorted_array = []
    i = 0
    j = 0

    num_inversions = 0

    while i < len(left_subarray) or j < len(right_subarray):
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
                num_inversions += (len(left_subarray) - i)
        elif j >= len(right_subarray):
            #If the right half has been fully traversed, append the remaining elements from the left half
            sorted_array.append(left_subarray[i])
            i = i + 1
        elif i >= len(left_subarray):
            #If the left half has been fully traversed, append the remaining elements in the right half
            sorted_array.append(right_subarray[j])
            j = j + 1

    return sorted_array, num_inversions


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()

    #Read in the text file of integers and store it in a list
    with open(Path(path, 'IntegerArray.txt')) as text_file:
        array = []
        for line in text_file:
            array.append(int(line))

    total_inversions = count_inversions(array)
    print(total_inversions)