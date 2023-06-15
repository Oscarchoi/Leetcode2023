class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        length = 0
        for i in range(len(nums) - 2):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                length += 1
                count += length
            else:
                length = 0
        return count
