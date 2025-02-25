#!/usr/bin/python3

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2] # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example Usage
numbers = [64, 34, 36, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("The Original Array:", numbers)
print("The Sorted array:", sorted_numbers)
