import random
  
array = [10, 7, 8, 9, 1, 5]

def quicksort(arr, start , stop):
    if(start < stop):        
        # pivotindex is the index where the pivot lies in the array
        pivotindex = partitionrand(arr, start, stop)
        # At this stage the array is partially sorted around the pivot. 
        # Separately sorting the left half of the array and the right half of the array.
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
  
# This function generates a random pivot
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start # pivot
    # a variable to memorize where the partition in the array starts from.
    i = start + 1 
      
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

quicksort(array, 0, len(array) - 1)
print(array)
