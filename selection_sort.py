#!/usr/bin/python3

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

                # Swap the found minimum element with the first element of unsorted part
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

            # Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)

# The algorithm divides the array into two parts: sorted (initially empty) and unsorted
