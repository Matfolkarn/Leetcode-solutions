class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums) - 1
        lower_bound = 0
        while lower_bound <= upper_bound:
            i = lower_bound + (upper_bound - lower_bound)//2
            n = nums[i]
            if n > target:
                upper_bound = i -1
            elif n < target:
                lower_bound = i + 1
            else:
                return i
        return -1