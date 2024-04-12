import time

def insertionSort(arr):
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
list = []
with open("numbers_100k.txt") as f:
    for line in f:
        list.append(line.split())

arr = list[0]
arr = [int(i) for i in arr]
size = len(arr)
start_time = time.time()
insertionSort(arr)
print(time.time() - start_time, 's')