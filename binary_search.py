#!/usr/bin/python3

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found the target
        if arr[mid] == target:
            return mid
        # Target is in the right half
        elif arr[mid] < target:
            left = mid + 1
        # Target is in the left half
        else:
            right = mid - 1
    return - 1 # Target not found

# Example usage 
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)
print(f"Target {target} found at index: {result}")


