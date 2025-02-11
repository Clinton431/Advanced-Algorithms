#!/usr/bin/python3

def linear_search(arr, target):
    """
    Performs linear search to find target in array.
    Returns index if found, -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1

def linear_search_all_occurrences(arr, target):
    """
    Finds all occurrences of target in array.
    Returns list of indices where target is found.
    """

    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
        return indices

    # Example usage with different scenarios
def demonstrate_linear_search():
    # Test case 1: Basic Search
    numbers = [4, 2, 7, 1, 9, 5, 3]
    target = 7
    result = linear_search(numbers, target)
    print(f"Test 1 - Finding {target} in {numbers}")
    print(f"Result: Found {target}")

    # Test Case 2: Element not Present
    target = 6
    result = linear_search(numbers, target)
    print(f"Test 2 - Finding {target} in {numbers}")
    print(f"Result: {result} (Not found)\n")

    # Test Case 3: Multiple occurrences
    numbers_with_duplicates = [2, 5, 2, 9, 2]
    target = 2
    result = linear_search_all_occurrences(numbers_with_duplicates, target)
    print(f"Test 3 - Finding all occurrences of {target} in {numbers_with_duplicates}")
    print(f"Result: Found at indices {result}\n")

    #Test Case 4: Empty array
    empty_array = []
    target = 5
    result = linear_search(empty_array, target)
    print(f"Test 3 - Finding {target} in empty array")
    print(f"Result: {result} (Not found)\n")

# Demonstration
demonstrate_linear_search()
