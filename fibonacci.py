# Python program to store roll numbers of student array who attended training program
# in sorted order and provide functions for searching using Binary search and Fibonacci search

# Function to perform Binary Search
def binary_search(arr, target):
    # Set the lower and upper bounds for the search
    low = 0
    high = len(arr) - 1

    # Loop until the lower bound is less than or equal to the upper bound
    while low <= high:
        # Calculate the midpoint of the current search range
        mid = (low + high) // 2

        # If the target is less than the element at the midpoint, search the left half
        if target < arr[mid]:
            high = mid - 1
        # If the target is greater than the element at the midpoint, search the right half
        elif target > arr[mid]:
            low = mid + 1
        # If the target is equal to the element at the midpoint, return True
        else:
            return True

    # If the target is not found, return False
    return False

# Function to perform Fibonacci Search
def fibonacci_search(arr, target):
    # Initialize the Fibonacci sequence and the search range
    fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    k = 0
    low = 0
    high = len(arr) - 1

    # Find the largest Fibonacci number less than or equal to the length of the array
    while fib_seq[k] < high:
        k += 1

    # Initialize the offset to be the kth element of the Fibonacci sequence
    offset = fib_seq[k]

    # Loop until the offset is greater than or equal to the length of the array
    while offset >= 1:
        # Calculate the midpoint of the current search range
        mid = low + offset

        # If the midpoint is out of range, set it to the upper bound of the array
        if mid > high:
            mid = high

        # If the target is less than the element at the midpoint, search the left half
        if target < arr[mid]:
            high = mid - 1
        # If the target is greater than the element at the midpoint, search the right half
        elif target > arr[mid]:
            low = mid + 1
        # If the target is equal to the element at the midpoint, return True
        else:
            return True

        # Calculate the next offset using the Fibonacci sequence
        offset = fib_seq[k - 1] - offset
        k -= 1

    # If the target is not found, return False
    return False

# Test the search functions
students = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

print(binary_search(students, 102)) # True
print(binary_search(students, 110)) # False

print(fibonacci_search(students, 102)) # True
print(fibonacci_search(students, 110)) # False
