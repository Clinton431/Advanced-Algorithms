#!/usr/bin/python3
def bubble_sort(arr):
    n = len(arr)                    # Get length of array

    # Traverse through all array elements
    for i in range(n):

        # Flag to optimize the algorithm
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swapping occurred in this pass, array is already sorted
        if not swapped:
            break

    return arr

# Example usage
if __name__ == "__main__":
    # Test case 1: Random array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    sorted_arr1 = bubble_sort(arr1.copy())
    print("Sorted array:", sorted_arr1)

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print("\nOriginal array:", arr2)
    sorted_arr2 = bubble_sort(arr2.copy())
    print("Sorted array:", sorted_arr2)

    # Test case 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print("\nOriginal array:", arr3)
    sorted_arr3 = bubble_sort(arr3.copy())
    print("Sorted array:", sorted_arr3)
