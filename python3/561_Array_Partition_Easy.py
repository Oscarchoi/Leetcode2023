# 561. Array Partition

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum([x for i, x in enumerate(nums) if (i % 2 == 1)])