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
