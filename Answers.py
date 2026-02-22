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
def find_leaders(arr):
    if not arr:
        return []

    n = len(arr)
    result = []
    max_right = arr[n - 1]
    result.append(max_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            result.append(arr[i])

    result.reverse()
    return result
##question no. 18) Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def move_zeroes(arr):
    result = []
    zero_count = 0

    for x in arr:
        if x == 0:
            zero_count += 1
        else:
            result.append(x)

    return result + [0] * zero_count
##question no. 19) Find Subarray with Given Sum.
def subarray_with_sum(arr, target):
    curr_sum = 0
    start = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        while curr_sum > target:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == target:
            return arr[start:end+1]

    return []

##question no. 20) Rotate Array to the Left by k Positions
def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)

    return arr

##question no. 21) Find the Kth Smallest Element
import heapq

def kth_smallest(arr, k):
    if k > len(arr) or k <= 0:
        return None

    heap = []

    for num in arr:
        heapq.heappush(heap, num)

    count = 1
    while count < k:
        heapq.heappop(heap)
        count += 1

    return heapq.heappop(heap)

##question no. 22) Find All Subarrays
def all_subarrays(arr):
    result = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            result.append(arr[i:j])

    return result

##question no. 23) Maximum Sum Subarray (Kadane's Algorithm)
def max_subarray_sum(arr):
    max_sum = arr[0]
    curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

##question no. 24) Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def rearrange_alternate(arr):
    arr.sort()
    result = []

    left = 0
    right = len(arr) - 1

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])

        left += 1
        right -= 1

    return result

##question no. 25) Find Majority Element: Find the element that appears more than n/2 times.
def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


##question no. 31) Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.
def equilibriumIndex(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]

        if left_sum == total_sum:
            return i

        left_sum += arr[i]

    return -1

##question no. 32)Find Maximum Product Pair: Find two elements whose product is maximum.
def maxProductPair(arr):
    arr.sort()
    n = len(arr)

    return max(arr[0] * arr[1], arr[n-1] * arr[n-2])

##question no. 33)  Find Maximum Difference (j > i)
## buy at low and sell at high  type question
def maxDifference(arr):
    min_element = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_element)
        min_element = min(min_element, arr[i])

    return max_diff
