import random
import time
import matplotlib.pyplot as plt
import timeit

def generate_random_array(size):
    """Generate a random array of given size"""
    return [random.randint(0, 999999) for _ in range(size)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Benchmarking function for individual sorting algorithms
def calculate_benchmark_algorithm(input_sizes):
    times = []
    insertion_times = []
    bubble_sort_times = []
    selection_sort_times = []
    for _ in range(input_sizes):
        # Generate a random array with a random size
        size = random.randint(100, 15000)  # Random size between 100 and 15000
        arr = generate_random_array(size) #Generate an array of the randomly generated size
        #print("Generated array: of size: ", arr, size)
        bubblesort_execution_time = timeit.timeit(lambda: bubble_sort(arr), number=1)
        selection_sort_execution_time = timeit.timeit(lambda: selection_sort(arr), number=1)
        insertion_sort_execution_time = timeit.timeit(lambda: insertion_sort(arr), number=1)
        print("time taken to sort :", bubblesort_execution_time,insertion_sort_execution_time,selection_sort_execution_time)  

        bubble_sort_times.append(bubblesort_execution_time)
        selection_sort_times.append(selection_sort_execution_time)
        insertion_times.append(insertion_sort_execution_time)
    times.append(bubble_sort_times)
    times.append(selection_sort_times)
    times.append(insertion_times)
    return times
        #bubble_sortedArr = bubble_sort(arr)
        #insertion_sortedArr = insertion_sort(arr)
        #selection_sortedArr = selection_sort(arr)
        #print("Sorted array using the algorithms bubble: insertion: selection: ", bubble_sortedArr,insertion_sortedArr,selection_sortedArr)
        

   

# Number of different input sizes to test
num_sizes = 2  # You can change this to test more random sizes
time_for_diff_sorting_algos = calculate_benchmark_algorithm(num_sizes)
print(time_for_diff_sorting_algos)


# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(size, time_for_diff_sorting_algos[1], label="Selection Sort", marker='o')
plt.plot(size, time_for_diff_sorting_algos[0], label="Bubble Sort", marker='x')
plt.plot(size, time_for_diff_sorting_algos[2], label="Insertion Sort", marker='^')
plt.xlabel('Random input sizes')
plt.ylabel('Time (seconds)')
plt.title('Benchmarking Sorting Algorithms with Random Input Sizes')
plt.legend()
plt.grid(True)
plt.show()
