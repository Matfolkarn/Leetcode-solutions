class Solution:
    def area(self, heights, ind1, ind2):
        return (ind2-ind1) * min(heights[ind1], heights[ind2])
    
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1

        m = 0
        while r > l:
            a = self.area(heights, l, r)

            if a > m:
                m = a
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return m
