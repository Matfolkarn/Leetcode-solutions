import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        l, r = 1 , max(piles)
        res = r

        while l <= r:
            mid = (l + r)//2

            res_h = 0
            for i in piles:
                res_h += math.ceil(float(i)/mid)
            if res_h > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid

        return res
