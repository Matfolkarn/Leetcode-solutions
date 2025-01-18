class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxheap, [dist,x,y])
        
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(maxheap)
            res.append([x,y])
        
        return res
