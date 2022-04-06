from random import randint, shuffle
import datetime
import numpy

def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    cf = 0

    while (start <= end):
        print(f"Subarray in step {step}: {str(array[start:end+1])}")
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid
            cf += 1
        if element < array[mid]:
            end = mid - 1
            cf += 1
        else:
            cf += 1
            start = mid + 1
    return -1
    print("CF: {}".format(cf))

n = int(input("Enter range: "))
res = [*range(n)]
shuffle(res)
res = sorted(res)

key = int(input("Key: "))
start = datetime.datetime.now()
print(binary_search_iterative(res, key))
print(f"Searching for {key} in {res}")
print(f"Index of {key}: {binary_search_iterative(res, key)}")
print(f'End time: {datetime.datetime.now() - start}')