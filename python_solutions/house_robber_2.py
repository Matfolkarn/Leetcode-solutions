class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]),
                    self.rob1(nums[:-1])
        )


    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        res = [0] * (n)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, n):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        return res[n-1]
