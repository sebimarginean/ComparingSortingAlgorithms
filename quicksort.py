import time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 

list = []
with open("numbers_1kk.txt") as f:
    for line in f:
        list.append(line.split())

arr = list[0]
arr = [int(i) for i in arr]
size = len(arr)
start_time = time.time()
quickSort(arr, 0, size-1)
print(time.time() - start_time, 's')
