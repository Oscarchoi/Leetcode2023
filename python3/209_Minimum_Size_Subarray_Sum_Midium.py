# 209. Minimum Size Subarray Sum - Medium

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        min_len = N + 1

        front = 0
        current = 0
        for idx in range(N):
            current += nums[idx]
            if current < target:
                continue
            while current >= target and front <= idx:
                min_len = min(idx - front + 1, min_len)
                current -= nums[front]
                front += 1

        return min_len if min_len != N + 1 else 0