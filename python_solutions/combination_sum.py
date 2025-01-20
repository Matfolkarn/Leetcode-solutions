class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, s):
            nonlocal res

            if i >= len(nums) or sum(s) > target:
                return
            elif sum(s) == target:
                res.append(s)
                return
            elif sum(s) < target:
                new_s = s.copy()
                new_s.append(nums[i])
                dfs(i, new_s)
            dfs(i + 1, s.copy())

        dfs(0, [])
        return res
