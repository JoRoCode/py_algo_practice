# Linear search

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
arr = [2,5,8,9,10,1,22,25]
target = 10

print(search(arr, target))

# Binry search - iterative 
# mostly works on sorted arr

def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid+1
        elif arr[mid]> target:
            end = mid -1
        else:
            return mid

arr = [2,5,8,9,10,1,22,25]
target = 10
result = binary_itr(arr,0,len(arr)-1, target)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
    
    
# Binry search - recursive

def binary_recur(arr,start,end,target):
    if end >=start:
        mid = start + end -1//2
        if arr[mid] < target:
            binary_recur(arr, mid+1, end, target)
        elif arr[mid] > target:
            return binary_recur(arr, start, mid-1, target)
        else:
            return mid
    else:
        return -1
    
    arr = [2,5,8,9,10,1,22,25]
target = 10
result = binary_recur(arr,0,len(arr)-1, target)

if result != 1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
    
# bubble sort
# built in ability to detect if a list is already sorted

def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            print(j)
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations
    
A = [9,8,7,6,5,4,3,2,1]
print(bubble_optimized(A))


# insertion sort

def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A
        
A = [5,2,4,6,1,3]
print(insert_sort(A))






