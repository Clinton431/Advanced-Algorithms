# Algorithm Implementations in Python

This repository contains implementations of various searching and sorting algorithms with detailed explanations, time complexity analysis, and practical examples.

## Table of Contents
1. [Overview](#overview)
2. [Algorithms Included](#algorithms-included)
3. [Getting Started](#getting-started)
4. [Structure](#structure)
5. [How to Use](#how-to-use)
6. [Contributing](#contributing)

## Overview
This project aims to provide clear, well-documented implementations of common algorithms. Each implementation includes:
- Detailed explanation of the algorithm
- Time and space complexity analysis
- Practical examples
- Test cases
- Performance comparisons where applicable

## Algorithms Included

### Searching Algorithms
1. Linear Search
   - Simple sequential search
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Best for: Small datasets, unsorted arrays

*(More algorithms will be added as implemented)*

## Getting Started

### Prerequisites
- Python 3.x
- No additional packages required

### Installation
```bash
git clone [repository-url]
cd algorithm-implementations
```

## Structure
```
algorithms/
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   └── ...
├── sorting/
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── ...
├── tests/
│   ├── test_linear_search.py
│   └── ...
└── README.md
```

## How to Use

### Running an Algorithm
```python
from searching.linear_search import linear_search

# Example usage
array = [4, 2, 7, 1, 9, 5, 3]
target = 7
result = linear_search(array, target)
print(f"Element found at index: {result}")
```

Binary Search Algorithm Analysis
Algorithm Description
Binary Search is a searching algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half, comparing the middle element with the target value, and eliminating the half where the target cannot lie.
Time Complexity

Best Case: O(1)

Occurs when the target element is at the middle of the array
Only requires one comparison


Average Case: O(log n)

Each iteration eliminates half of the remaining elements
For an array of size n, requires approximately log₂(n) comparisons


Worst Case: O(log n)

Occurs when the target element is at either end of the array or not present
Requires log₂(n) comparisons to determine the element's presence or absence



Space Complexity

Iterative Implementation: O(1)

Only requires a constant amount of extra space for variables (left, right, mid)
No additional data structures needed


Recursive Implementation: O(log n)

Requires space on the call stack proportional to the number of recursive calls
Each recursive call stores local variables

# Sorting Algorithms
# Sorting Algorithms

## What Are Sorting Algorithms?
Sorting algorithms are methods used to arrange elements in a specific sequence or order, typically in ascending or descending order. They are fundamental to computer science and are used extensively in various applications to organize and structure data efficiently.

## Common Sorting Algorithms

### 1. Bubble Sort
- **How it works**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Used When**: 
  - Working with small datasets
  - Teaching sorting concepts
  - Memory space is limited

### 2. Quick Sort
- **How it works**: Uses a divide-and-conquer strategy by selecting a 'pivot' element and partitioning the array around it.
- **Time Complexity**: Average O(n log n), Worst O(n²)
- **Space Complexity**: O(log n)
- **Best Used When**:
  - Working with large datasets
  - Memory space is not a constraint
  - Average-case performance is important

### 3. Merge Sort
- **How it works**: Divides the array into smaller subarrays, sorts them, and then merges them back together.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Best Used When**:
  - Stable sorting is required
  - Working with linked lists
  - External sorting is needed

### 4. Selection Sort
- **How it works**: Repeatedly finds the minimum element from the unsorted portion and places it at the beginning.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Used When**:
  - Memory writing needs to be minimized
  - Working with small arrays
  - Simplicity is preferred over efficiency

### 5. Insertion Sort
- **How it works**: Builds the final sorted array one item at a time by repeatedly inserting elements in their correct position.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Used When**:
  - Working with small datasets
  - Data is nearly sorted
  - Online sorting (sorting data as it is received)

## Real-World Use Cases

### 1. Database Management
- Sorting records for efficient retrieval
- Organizing data in indexes
- Optimizing query results

### 2. File Systems
- Organizing files and directories
- Maintaining sorted file listings
- Managing file hierarchies

### 3. User Interfaces
- Sorting items in lists or tables
- Organizing menu items
- Arranging elements alphabetically

### 4. Data Analysis
- Organizing datasets for analysis
- Preparing data for visualization
- Statistical computations

### 5. Operating Systems
- Process scheduling
- Memory management
- File organization

### 6. E-commerce
- Product listing by price
- Sorting search results
- Customer ratings organization

## Selection Guide

Choose your sorting algorithm based on:

1. **Data Size**
   - Small data (< 50 elements): Insertion Sort, Bubble Sort
   - Medium data: Quick Sort, Merge Sort
   - Large data: Quick Sort, Merge Sort

2. **Memory Constraints**
   - Limited memory: Bubble Sort, Selection Sort
   - Adequate memory: Quick Sort, Merge Sort

3. **Data Characteristics**
   - Nearly sorted data: Insertion Sort
   - Random data: Quick Sort
   - Linked list: Merge Sort

4. **Stability Requirements**
   - Stable sorting needed: Merge Sort, Insertion Sort
   - Stability not important: Quick Sort, Selection Sort

## Performance Comparison

| Algorithm      | Best Case  | Average Case | Worst Case | Space      | Stable |
|---------------|------------|--------------|------------|------------|--------|
| Bubble Sort   | O(n)       | O(n²)        | O(n²)      | O(1)       | Yes    |
| Quick Sort    | O(n log n) | O(n log n)   | O(n²)      | O(log n)   | No     |
| Merge Sort    | O(n log n) | O(n log n)   | O(n log n) | O(n)       | Yes    |
| Selection Sort| O(n²)      | O(n²)        | O(n²)      | O(1)       | No     |
| Insertion Sort| O(n)       | O(n²)        | O(n²)      | O(1)       | Yes    |

# Bubble Sort
Bubble Sort
Think of it like sorting a deck of cards where you repeatedly go through the deck, comparing two cards at a time. If they're in the wrong order, you swap them. The larger numbers "bubble up" to the end of the array, like bubbles rising in water. It's simple but inefficient for large datasets.

The Main Function:

Takes an array as input
Uses two nested loops to compare and swap elements
Returns the sorted array


The Algorithm Steps:

Compare adjacent elements (arr[j] and arr[j+1])
If they are in the wrong order, swap them
Continue this process for each pair of adjacent elements to the end
After each iteration, the largest unsorted element moves to its correct position


Optimization:

The swapped flag helps optimize the algorithm
If no swaps occur in a pass, the array is already sorted
We can break out of the loop early


Time Complexity:

Worst and Average Case: O(n²)
Best Case (when array is already sorted): O(n)


Space Complexity:

O(1) as it only uses a constant amount of extra space



To test this code, you can run it directly. The output will look something like this:

 Bubble Sort

# How it works: Repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.
# Time Complexity: O(n²)
# Space Complexity: O(1)
# Best Used When:

## Working with small datasets
## Teaching sorting concepts
## Memory space is limited

## Selection Sort
# Selection Sort Algorithm

## Overview
Selection Sort is a simple comparison-based sorting algorithm. It divides the input array into two portions: a sorted portion and an unsorted portion. The algorithm repeatedly selects the smallest element from the unsorted portion and adds it to the sorted portion.

## Time Complexity
- Worst Case: O(n²)
- Average Case: O(n²)
- Best Case: O(n²)

## Space Complexity
- O(1) - Selection Sort is an in-place sorting algorithm

## Advantages
1. Simple implementation
2. Works well with small datasets
3. Performs well on arrays that are already partially sorted
4. Memory efficient with O(1) space complexity
5. Minimal memory writes compared to other algorithms

## Disadvantages
1. Poor performance on large datasets due to O(n²) time complexity
2. Not stable - might change the relative order of equal elements
3. No early termination - must complete all iterations even if array is sorted

## Implementation

```python
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
```

## Usage Example
```python
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

## Algorithm Steps
1. Start with the first element as the minimum
2. Search the minimum element in the remaining unsorted array
3. Swap the found minimum with the first element of unsorted part
4. Move the boundary of sorted array one element forward
5. Repeat steps 1-4 until the entire array is sorted

## Performance Comparison
| Metric | Performance |
|--------|-------------|
| Time Complexity (Worst) | O(n²) |
| Time Complexity (Average) | O(n²) |
| Time Complexity (Best) | O(n²) |
| Space Complexity | O(1) |
| Stability | Unstable |

## Applications
- Small datasets where simple implementation is preferred
- Systems with limited memory where in-place sorting is required
- Educational purposes to understand basic sorting concepts
- When the cost of swapping elements is high (makes fewer swaps than bubble sort)

# Jump Search Algorithm

## Overview
Jump Search is an efficient searching algorithm designed for sorted arrays. It works by skipping a fixed number of elements and jumping ahead by steps, making it especially efficient for large datasets where binary search might be overkill and linear search too slow.

## Time Complexity
- Worst Case: O(√n)
- Average Case: O(√n)
- Best Case: O(1)

## Space Complexity
- O(1) - Jump Search is performed in-place

## Advantages
1. Better than linear search (O(n))
2. Particularly useful for large datasets
3. Works well when the element is closer to the beginning
4. Good for systems where jumping back is cheaper than reading elements
5. Simpler than binary search implementation

## Disadvantages
1. Only works on sorted arrays
2. Not as fast as binary search for most cases
3. Less efficient when target is towards the end of array
4. Performance depends heavily on the size of the jump step

## Implementation

```python
import math

def jump_search(arr, target):
    n = len(arr)
    # Finding the optimal jump step size
    step = int(math.sqrt(n))
    
    # Finding the block where the element is present
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    # If element is found
    if arr[prev] == target:
        return prev
    
    return -1
```

## Usage Example
```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = jump_search(arr, target)
print(f"Number {target} is at index {result}")  # Output: Number 6 is at index 6
```

## Algorithm Steps
1. Determine the optimal jump size (√n)
2. Jump ahead by the jump size until finding a value greater than the target
3. Perform linear search in the block where target might exist
4. Return the index if found, -1 if not found

## Performance Comparison
| Algorithm | Time Complexity | Space Complexity | Sorted Array Required |
|-----------|----------------|------------------|----------------------|
| Jump Search | O(√n) | O(1) | Yes |
| Linear Search | O(n) | O(1) | No |
| Binary Search | O(log n) | O(1) | Yes |

## Best Use Cases
1. Large sorted datasets
2. Systems with expensive backward operations
3. When target elements are likely to be at the beginning
4. Memory-constrained environments
5. When implementation simplicity is preferred over optimal speed

## Real-world Applications
- Database searching where records are sorted
- File systems with sorted directories
- Search in memory-mapped files
- Mobile applications where binary search might be computational overkill

## Code Optimization Tips
1. Choose optimal jump size based on data size
2. Consider data distribution when selecting jump size
3. Implement bounds checking for array safety
4. Use early termination when possible
5. Consider cache-friendly implementations for large datasets

## Contributing
Contributions to improve the implementation or documentation are welcome. Please ensure any modifications maintain the O(√n) time complexity.


### Running Tests
```bash
python -m unittest tests/test_linear_search.py
```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/algorithm-name`)
3. Implement your algorithm
4. Add appropriate tests
5. Update documentation
6. Submit a pull request

### Contribution Guidelines
- Follow PEP 8 style guide
- Include docstrings for all functions
- Add comprehensive test cases
- Update README with new algorithm details
- Include time and space complexity analysis

## License
This project is licensed under the MIT License - see the LICENSE file for details.
