class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        
        for n in range(1,len(nums)):
            prefix[n] = prefix[n-1] * nums[n-1]
        
        postfix = [1] * (len(nums) + 1)
        for n in range(len(nums) - 1, -1, -1):
            print(n)
            postfix[n] = postfix[n+1] * nums[n]
        
        res = []
        print(prefix)
        print(postfix)
        for n in range(len(nums)):
            
            res.append(prefix[n]*postfix[n+1])

        return res