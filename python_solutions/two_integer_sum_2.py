class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            diff = target - numbers[n]
            if diff in numbers:
                return [n+1, numbers.index(diff) +1]