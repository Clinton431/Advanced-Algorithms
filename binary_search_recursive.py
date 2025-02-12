#!/usr/bin/python3

def binary_search_recursive(arr, left, right, target):
    if left > right:
        print(f"{target} not found in the list.")
        return - 1  # Base case: target not found

    mid = (left + right) // 2
    print(f"Searching in range {arr[left:right+1]}, Middle index: {mid}, Middle value: {arr[mid]}")

    if arr[mid] == target:
          print(f"Found {target} at index {mid}!")
          return mid # Target found
    elif arr[mid] < target:
          return binary_search_recursive(arr, mid + 1, right, target) # Search in the right half
    else:
          return binary_search_recursive(arr, left, mid - 1, target) # Search in the left half


    # Example usage
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # Sorted list
target = 25 # Searching for 25
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
          print(f"Element  found at index {result}")
else:
          print("Element not found")
