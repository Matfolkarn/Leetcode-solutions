class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            new_s = s1 - s2

            if new_s != 0:
                heapq.heappush(max_heap, new_s)

        if len(max_heap) > 0:
            return -heapq.heappop(max_heap)
        else:
            return 0

