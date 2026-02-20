## question no. 1)Reverse an Array
import numpy as np 
from numpy import array
def array_rev(arr,res , n):
    len(arr) = n
    res = []
    for i in range(n, -1 , -1):
        arr[-1:] = res
    return res

##question no. 2) Find the Maximum & Minimum Element
def max_min(arr , n , ,  maxi , mini):
    len(arr) = n
    maxi = float("-inf")
    mini = float("inf")
    for i in range(0,n):
        if arr[i] > max:
            max = arr[i]
            i+=1
        
        elif arr[i] < min:
            min = arr[i]
            i+=1
            return min
    return max

##question no. 3) Find the Sum of Elements
def sum_arr(arr,n , ):
    len(arr) = n
    for i in range(0 , n):
        sums += arr[i]
        i+=1
    return sums ## because sum is a built-in function

##question no. 4) Find the Second Largest Element
def sec_large(arr,n , maxi , sec_maxi):
    len(arr) = n
    maxi = float("-inf")
    sec_maxi = float("-inf")
    for i in range(0 ,n):
        if arr[i] > maxi:
            maxi = arr[i]
            i+=1
            if arr[i] < maxi and arr[i] > sec_maxi:
                sec_maxi = arr[i]
    return sec_maxi

##question no. 5) Count Frequency of Elements
def count(arr,n ,freq):
    len(arr) = n
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for k, v in freq.items():
        print(f"{k} → {v}")

##question no. 6) Check if Array is Sorted
def sort_arr(arr , n):
    len(arr) = n
    for i in range(0 ,n):
        if arr[i] < arr[i+1]:
            i+=1
        return True
    else:
        return False

##question no. 7) Rotate Array by k Positions: Rotate the array to the right by k positions.
def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        
        reverse(0, n - 1)
       
        reverse(0, k - 1)
        
        reverse(k, n - 1)

##question no. 8) Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def pair_sum(arr , n , target , res):
    n = len(arr)
    x =target
    res = []
    for i in range(0 , n):
        for j in range(i+1 , n):
            if arr[i] + arr[j] == target:
                res.append((arr[i], arr[j]))               
            else:
                return -1
    return res

##question no. 9) Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
#assuming there are duplicates and array is jumpled not sorted in case of sorted array T.C. will be less
def duplicates(arr , n ,res):
    n = len(arr)
    res = []
    arr = arr.sort()
    for i in range(0 , n):
        if arr[i] != arr[i+1]:
            res.append(arr[i])
        else:
            i+=1
    return res

##question no. 10) Merge Two Sorted Arrays
## Considering the two arrays are sorted and we have to merge them into a single sorted array
def merge(arr1 , arr2 , n , m ,res):
    n = len(arr1)
    m = len(arr2)
    res = []
    i = j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i < n:
        res.append(arr1[i])
        i+=1
    while j < m:
        res.append(arr2[j])
        j+=1
        return res
    
##question no. 11) Remove given Element from Array
def remove_ele(arr , n , target , res):
    n =len(arr)
    x = target
    res = []
    for i in range(0,n):
        if arr[i] != target:
            res.append(arr[i])
        else:
            i+=1
    return res

##question no. 12)  Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def missing_num(arr , n ,res):
    n = len(arr)
    res = []
    for  i in range(1,n+1):
        if arr[i] !=i:
            res.append(i)
        else:
            i+=1
    return res

##question no. 13)Find Duplicates in an Array: Find all duplicate elements in the array.
def find_dup(arr , n , res):
    n = len(arr)
    res =[]
    arr.sort()
    for i in range(0 , n):
        if arr[i] == arr[i+1]:
            res.append(arr[i])
            i+=2
        else:
            i+=1
    return res

##question no. 14) Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2 , n , m , res):
    n = len(arr1)        
    m = len(arr2)  
    res  = []
    arr1.sort()
    arr2.sort()
    for i in range(0 , n):
        for j in range(0,m):
            if arr1[i] == arr2[j]:
                res.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i] <= arr2[j]:
                i+=1
            elif arr1[i] > arr2[j]:
                j+=1
            else:
                return -1
    return res

##question no. 15) Find Union of Two Arrays: Find all unique elements from both arrays.

def union(arr1, arr2 , n , m , res): 
    n = len(arr1)        
    m = len(arr2)  
    res  = []
    arr1.sort()
    arr2.sort()
    i = j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j+=1
        else:
            res.append(arr1[i])
            i+=1
            j+=1
    while i < n:
        res.append(arr1[i])
        i+=1
    while j < m:
        res.append(arr2[j])
        j+=1
    return list(set(res))

##question no. 16) Check if Two Arrays Are Equal: if two arrays contain the same elements
def are_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    freq = {}

    for i in range(len(arr1)):
        if arr1[i] in freq:
            freq[arr1[i]] = freq[arr1[i]] + 1
        else:
            freq[arr1[i]] = 1

    for j in range(len(arr2)):
        if arr2[j] not in freq:
            return False

        freq[arr2[j]] = freq[arr2[j]] - 1

        if freq[arr2[j]] < 0:
            return False

    return True  

##question no. 17)Find the Leader Elements: An element is a leader if it is greater than all elements to its right