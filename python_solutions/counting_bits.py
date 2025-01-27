class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n +1):
            
            i = num
            r = 0
            while i:
                r += i%2
                i = i >> 1

            res.append(r)
        return res
