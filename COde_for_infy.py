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


