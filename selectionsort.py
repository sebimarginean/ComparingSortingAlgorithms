import time

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

list = []
with open("numbers_100k.txt") as f:
    for line in f:
        list.append(line.split())

arr = list[0]
arr = [int(i) for i in arr]

size = len(arr)
start_time = time.time()
selectionSort(arr, size)
print(time.time() - start_time, 's')