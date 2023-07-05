# 1493. Longest Subarray of 1's After Deleting One Element - Medium

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        prev = 0
        current = 0
        for num in nums:
            if num != 0:
                current += 1
                longest = max(longest, prev + current)
            else:
                prev = current
                current = 0

        if longest == len(nums):
            return longest - 1

        return longest