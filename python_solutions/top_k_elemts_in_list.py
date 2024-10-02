class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1   
        sorted_list = sorted(nums_dict.items(), key=lambda item: item[1])
        out = [x[0] for x in sorted_list[-k:]]
        return out