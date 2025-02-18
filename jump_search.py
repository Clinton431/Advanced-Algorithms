#!/usr/bin/python3

import math

def jump_search(arr, target):
    n = len(arr)
    # Finding the optimal jump step size
    step = int(math.sqrt(n))

    # Finding the block where the element is present (if it exist)
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

        # Doing linear search for target in block begining with prev
        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return  -1

            # If element is found
            if arr[prev] == target:
                return prev

            return -1

# Example usage
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 6
result = jump_search(arr, target)
print(f"Number {target} is at index {result}")  # Output: Number 6 is at index 6
