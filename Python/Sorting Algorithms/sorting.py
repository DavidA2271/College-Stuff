import random
import time


def create_array(size):
    ''' Creates an array of the input size. '''
    return [random.randint(0, 1000000) for _ in range(size)]


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j      
        array[i], array[min_index] = array[min_index], array[i]
    print("Done Selection")
    return array


def bubble_sort(array):
    arr_size = len(array)
    for i in range(arr_size):
        swapped = False
        for j in range(0, arr_size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            break
    print("Done Bubble")
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        curr_val = array[i]
        j = i - 1
        while j >= 0 and curr_val < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr_val
    print("Done Insertion")
    return array


def radix_sort(array):
    max_val = max(array)
    exp = 1
    while max_val / exp >= 1:
        arr_size = len(array)
        output = [0] * (arr_size)
        count = [0] * (10)
        for i in range(0, arr_size):
            index = array[i] // exp
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = arr_size - 1
        while i >= 0:
            index = array[i] // exp
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(0, len(array)):
            array[i] = output[i]
        exp *= 10
    print("Done Radix")
    return array


def time_sort(array, sort_method):
    ''' Returns the time it takes to run a sorting method. '''
    start = time.time()
    sort_method(array)
    end = time.time()
    return end - start


def time_sort_all(array):
    ''' Runs all sort methods on an input array '''
    arr_size = len(array)

    sel_time = time_sort(array, selection_sort)
    bub_time = time_sort(array, bubble_sort)
    ins_time = time_sort(array, insertion_sort)
    rad_time = time_sort(array, radix_sort)
    default_time = time_sort(array, sorted)

    print()
    print(f"Selection sort took {sel_time} seconds to sort an array of size {arr_size}")
    print(f"Bubble sort took {bub_time} seconds to sort an array of size {arr_size}")
    print(f"Insertion sort took {ins_time} seconds to sort an array of size {arr_size}")
    print(f"Radix sort took {rad_time} seconds to sort an array of size {arr_size}")
    print(f"Python built-in sort took {default_time} seconds to sort an array of size {arr_size}")
    print()


if __name__ == '__main__':
    array1 = create_array(10**2)
    array2 = create_array(10**3)
    array3 = create_array(10**4)
    array4 = create_array(10**5)
    array5 = create_array(10**6)
    time_sort_all(array1)
    time_sort_all(array2)
    time_sort_all(array3)
    time_sort_all(array4)
    time_sort_all(array5)