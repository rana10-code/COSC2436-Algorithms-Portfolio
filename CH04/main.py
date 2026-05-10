def quicksort(array):
    """
    Sort an array using the quicksort algorithm.
    
    Args:
        array: List of numbers to sort
        
    Returns:
        Sorted list
    """
    # Base case
    if len(array) < 2:
        return array
    
    # Choose pivot
    pivot = array[0]
    
    # Partition
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    
    # Recurse and combine
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    # Test cases
    print(quicksort([10, 5, 2, 3]))
    print(quicksort([33, 15, 10]))
    print(quicksort([3, 5, 2, 1, 4]))
    print(quicksort([1]))
    print(quicksort([]))
    print(quicksort([8, 7, 6, 5, 4, 3, 2, 1]))
