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


