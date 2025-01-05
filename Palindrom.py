def is_palindrome_iterative(array):
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] != array[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_recursive(array, left, right):
    if left >= right:
        return True
    if array[left] != array[right]:
        return False
    return is_palindrome_recursive(array, left + 1, right - 1)

def measure_execution_time(func, array):
    start_time = Time.time()
    func(array)
    end_time = Time.time()
    return end_time - start_time

# Manual implementation of a basic time module
class Time:
    @staticmethod
    def time():
        import time
        return time.time()

# Adjust recursion limit for large arrays
class Sys:
    @staticmethod
    def setrecursionlimit(limit):
        import sys
        sys.setrecursionlimit(limit)

Sys.setrecursionlimit(1000000)

# Generate test cases with specific sizes
sizes = [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 100000, 500000, 1000000]
test_cases = []
for size in sizes:
    case = [i % 10 + 1 for i in range(size)]
    half_size = size // 2
    case[:half_size] = case[-half_size:][::-1]
    test_cases.append(case)

# Measure execution time for both algorithms
iterative_times = []
recursive_times = []

def measure_recursive(array):
    return is_palindrome_recursive(array, 0, len(array) - 1)

for case in test_cases:
    iterative_times.append(measure_execution_time(is_palindrome_iterative, case))
    recursive_times.append(measure_execution_time(lambda arr: is_palindrome_recursive(arr, 0, len(arr) - 1), case))

# Display results
print("\nExecution Time (in seconds):")
print("Size\tIterative\tRecursive")
for size, it_time, rec_time in zip(sizes, iterative_times, recursive_times):
    print(f"{size}\t{it_time:.6f}\t{rec_time:.6f}")
