class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        res = 0
        stack = []

        for h in range(len(heights)):

            start = h

            while len(stack) > 0 and stack[-1][1] > heights[h]:
                i, he = stack.pop()
                res = max(res, he*(h-i))
                start = i

            stack.append((start,heights[h]))
        
        print(stack)
        for i, h in stack:
            res = max(res, (len(heights) -i) * h)
        return res
