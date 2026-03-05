# Min swaps to make an array parity(SUMMER ARRAY)
class Solution:
    def min_swaps(self, nums: list[int]) -> int:
        def cost(nums , parityFirst):
            swaps = 0
            pos = 0
            for i in range(len(nums)):
                if  nums[i] % 2 == parityFirst:
                    pos+=1 
                    swaps+= abs(i - pos)
            return swaps
        odd_first = cost(nums , 1)
        even_first = cost(nums , 0)
        return min(odd_first , even_first)
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(min_swaps(nums))

##Count Distinct substrings with exactly k distinct characters
class solution:
    def count_distinct_substrings(self, s: str, k: int) -> int:
        n = len(s)
        result = set()
        for i in range(n):
            freq = {}
            unique_count = 0
            for j  in range(i , n):
                c = s[j]
                freq[c] = freq.get(c , 0) +1
                if freq[c] == 1:
                    unique_count+=1
                elif freq[c] == k:
                    result.add(s[i:j+1])
                if unique_count > k:
                    break
        return len(result)
    s = input().strip()
    k = int(input().strip())
    print(count_distinct_substrings(s , k))

## shortest path in unweighted graph
from collections import deque
class Solution:
    def shortest_path(self, edges ,graph):
        adj = [[] for _ in range(len(graph))]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1] * len(graph)
        dist[0] = 0
        queue = deque([0])
        while queue:
            u= queue.popleft()
            for u in adj[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] +1
                    queue.append(u)
            return dist
    n = int(input().strip())
    m = int(input().strip())
    edges = [list(map(int, input().strip().split())) for _ in range(m)]
    graph = [0] * n


""""
delivery Analytics — Count Revenue Windows

Situation: A delivery company tracks daily revenues from individual orders (positive or negative when refunds occur). For a revenue target K, they want to know how many contiguous periods (subarrays of days) achieved exactly that revenue.

Problem
Given an integer array revenues[] and integer K, return the total number of contiguous subarrays whose sum equals K
"""

class Solution:
    def count_revenue_periods(revenues , K):
        freq  = {0:1}
        prefix_sum =0
        subarr = 0

        for val in revenues:
            prefix_sum+=val
            if (prefix_sum -K) in freq:
                subarr += freq[prefix_sum - K]
            freq[prefix_sum] = freq.get(prefix_sum, 0) +1
        return subarr
    N,K = map(int , input.split())
    revenues =list(map(int,input().strip().split()))
    print(count_revenue_periods(revenues , K))

                
"""
User Session — Longest Unique Action Sequence

Situation: A product team records user action logs (characters representing actions). They want the longest continuous sequence of actions without repetition to study engagement.

Problem
Given string S representing user actions, find the length of the longest substring without repeating characters.

Input
S
1 ≤ len(S) ≤ 10^5
Characters are ASCII (or limited alphabet).

Output
Single integer — the length of longest substring with all distinct characters.

"""
class Solution:
    def longest_unique_actions(S):
        left = 0
        max_len = 0
        seen = set()
        
        for right in  range(len(S)):
            while S[right] in seen:
                seen.remove(S[left])
                left+=1
            seen.add(S[right])
            max_len = max(max_len , right - left + 1)
        return max_len
    S= input().strip()
    print(longest_unique_actions(S))

"""
Scheduling — Merge Overlapping Time Slots

Situation: A scheduler receives many proposed meeting time slots and needs to merge overlapping slots so rooms can be allocated efficiently.

Problem
Given N intervals [start, end], merge all overlapping intervals and output the merged list sorted by start time.
"""
class Solution:
    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]
        for s , e in intervals[1:]:
            last_s , last_e = merged[-1]
            if s<= last_e:
                if e> last_e:
                    merged[-1] = (last_s , e)
            else:
                merged.append((s,e))
        return merged
    N= int(input().strip())
    intervals = [tuple(map(int , input().strip().split())) for _ in range(N)]
    result = merge_intervals(intervals)
    print(len(result))
    for s ,e in result:
        print(s , e)

"""
Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish. He wants to choose as many dishes as possible from the given list but while satisfying two conditions:

He can choose only one type of dish.
No two chosen dishes should be adjacent to each other.
Ramu wants to know which type of dish he should choose from, so that he can pick the maximum number of dishes.

Example :

Given N= 9 and A= [1,2,2,1,2,1,1,1,1]

For type 1, Ramu can choose at most four dishes. One of the ways to choose four dishes of type 1 is A1,A4, A7 and A9.

For type 2, Ramu can choose at most two dishes. One way is to choose A3 and A5.

So in this case, Ramu should go for type 1, in which he can pick more dishes.

INPUT FORMAT:

The first line contains T, the number of test cases. Then the test cases follow.
For each test case, the first line contains a single integer N.
The second line contains N integers A1,A2,…,AN.
OUTPUT FORMAT

For each test case, print a single line containing one integer ― the type of the dish that Ramu should choose from. If there are multiple answers, print the smallest one.

CONSTRAINTS :

1 <= T <= 10^3
1 <= N <= 10^3
1 <= Ai <= 10^3
"""
class Solution:
    def max_dishes(n,item):
        n = int(input().strip())
        item = list(map(int,input().strip().split()))
        max_count = 0
        item_type = item[0]
        j=0
        while j<n:
            c=1
            k = j+1
            while k < n:
                if item[j] == item[k] and k != j+1: # equal but not adjacent
                    c +=1
                    if k < n and item[k] == item[k+1]:
                        k+=1
                k+=1
            if max_count < c:
                max_count = c
                item_type = item[j]
            j+=1
        print(item_type)
    t = int(input().strip())
    for _ in range(t):
        max_dishes(n , item)

"""
There are three piles of stones. The first pile contains a stones, the second pile contains b stones and the third pile contains c stones. You must choose one of the piles and split the stones from it to the other two piles; specifically, if the chosen pile initially contained s stones, you should choose an integer k (0≤k≤s), move k stones from the chosen pile onto one of the remaining two piles and s−k stones onto the other remaining pile. Determine if it is possible for the two remaining piles (in any order) to contain x stones and y stones respectively after performing this action.

INPUT FORMAT :

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains five space-separated integers 
          a,b,c, x and y.

OUTPUT FORMAT :

For each test case, print a single line containing the string “YES” if it is possible to obtain piles of the given sizes or “NO” if it is impossible.
"""
class Solution:
    def solve(a,b,c,x,y):
        a,b,c,x,y = map(int ,input().strip().split())
        if (a+b+c) != (x+y):
            print ("NO")
        else:
            if y  < min(a,b,c) or x < min(a,b,c):
                print("NO")
            else:
                print("YES")
    t = int(input().strip())
    for _ in range(t):
        solve(a,b,c,x,y)



