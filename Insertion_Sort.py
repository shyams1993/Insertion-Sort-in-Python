arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def insertionSort(arr):
    start = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] < start:
            holder = arr.pop(i)
            for x in range(0,i):
                if holder < arr[x]:
                    arr.insert(x,holder)
                    break
        start = arr[i]
        i+=1
    return arr
print(insertionSort(arr))