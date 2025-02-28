#!/usr/bin/python3
def insertion_sort(arr):
    """
    Implementation of the insertion sort algorithm.

    Args:
        arr: The input array to be sorted

    Returns:
        The sorted array

    Time Complexity:
        - Best Case: O(n) when array is already sorted
        - Average Case: O(n²)
        - Worst Case: O(n²) when array is sorted in reverse order

    Space Complexity: O(1) - sorts in-place
    """
    # Loop through array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Store the current element as our key
        key = arr[i]

        # Initialize j to point to the element before the key
        j = i - 1

        # Move elements greater than key one position ahead
        # This creates the correct position for our key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1               # Move to the previous element

        # Place the key in its correct position in the sorted sequence
        arr[j + 1] = key

    return arr


def insertion_sort_with_steps(arr):
    """
    Implementation of insertion sort that prints each step for educational purposes.

    Args:
        arr: The input array to be sorted

    Returns:
        The sorted array
    """
    print(f"Initial array: {arr}")

    # Loop through array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Store the current element as our key
        key = arr[i]

        print(f"\nStep {i}: Insert element {key} into the sorted portion {arr[:i]}")

        # Initialize j to point to the element before the key
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            print(f"  Shift {arr[j]} to the right")
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1               # Move to the previous element

        # Place the key in its correct position in the sorted sequence
        arr[j + 1] = key
        print(f"  Place {key} at position {j+1}")
        print(f"  Current array: {arr}")

    print(f"\nFinal sorted array: {arr}")
    return arr


# Example usage
if __name__ == "__main__":
    # Test with various arrays
    test_cases = [
        [12, 11, 13, 5, 6],
        [5, 2, 4, 6, 1, 3],
        [31, 41, 59, 26, 41, 58],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1]   # Reverse sorted
    ]

    print("=== Basic Insertion Sort ===")
    for i, test_array in enumerate(test_cases):
        print(f"\nTest case {i+1}:")
        original = test_array.copy()
        print(f"Original: {original}")
        sorted_array = insertion_sort(test_array.copy())
        print(f"Sorted:   {sorted_array}")

    print("\n\n=== Insertion Sort with Step-by-Step Explanation ===")
    insertion_sort_with_steps([5, 2, 4, 6, 1, 3])
