class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, s):
            
            nonlocal res
            if i >= len(nums):
                res.append(s)
                return
            dfs(i + 1, s.copy())
            new_s = s.copy()
            new_s.append(nums[i])
            dfs(i+1, new_s)
        dfs(0, [])
        return res
