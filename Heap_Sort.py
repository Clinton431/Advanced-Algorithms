#!/usr/bin/python3

def heapify(arr, n, i):
    """
    Convert a binary tree to a max heap at the given index i.
    
    Args:
        arr: The array to heapify
        n: Size of the heap
        i: The index of the node to heapify
    """
    # Initialize largest as root
    largest = i
    
    # Calculate the indices of the left and right children
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sort an array using the heap sort algorithm.
    
    Args:
        arr: The array to sort
        
    Returns:
        The sorted array (sorted in-place)
    """
    n = len(arr)
    
    # Build a max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    
    return arr


# Example usage
if __name__ == "__main__":
    test_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_array)
    
    sorted_array = heap_sort(test_array)
    print("Sorted array:", sorted_array)
