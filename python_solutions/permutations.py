class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        def rec(arr, res):
            if len(arr) == 0:
                nonlocal r
                r.append(res)
                return
        
            for x in range(len(arr)):
                arc = arr.copy()
                p = arc.pop(x)
                re = res.copy()
                re.append(p)
                rec(arc, re)
                
        rec(nums, [])
        return r
