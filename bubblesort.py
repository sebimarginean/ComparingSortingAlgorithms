import time

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
list = []
with open("numbers_100k.txt") as f:
    for line in f:
        list.append(line.split())

arr = list[0]
arr = [int(i) for i in arr]

start_time = time.time()
bubbleSort(arr)
print(time.time() - start_time, 's')