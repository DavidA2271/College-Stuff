# Results
### 100 elements
Selection Sort: 0.0005 seconds
Bubble Sort: 0.0 seconds
Insertion Sort: 0.0 seconds
Radix Sort: 0.0005 seconds
Built-in: 0.0 seconds

### 1000 elements
Selection Sort: 0.135 seconds
Bubble Sort: 0.0 seconds
Insertion Sort: 0.0 Seconds
Radix Sort: 0.015 seconds
Built-in: 0.0 seconds

### 10000 elements
Selection Sort: 1.2774 seconds
Bubble Sort: 0.0005 seconds
Insertion Sort: 0.0010 seconds
Radix Sort: 0.0110 seconds
Built-in: 0.0 seconds

### 100000 elements
Selection Sort: 331.5962 seconds
Bubble Sort: 301.3332 seconds
Insertion Sort: 0.0095 seconds
Radix Sort: 0.1267 seconds
Built-in: 0.0010 seconds

### 1000000 elements
Did not run because Selection and bubble sorts were taking too long.


# Analysis
### Selection Sort
Much slower than the rest. Makes sense due to its O(n^2) time complexity.
### Bubble Sort
Also very slow, but faster than selection sort. Took a lot longer upon reaching 100000 elements.
### Insertion Sort
Seems to be the fastest of the sorting methods. Very similar times to the built-in python sorting method.
### Radix Sort
Also very fast, but not as fast as the Insertion Sort.

# Hypothesis
I think Python uses the Insertion ssort algorithm for sorting its lists. The time stamps are most similar to insertion sort.

