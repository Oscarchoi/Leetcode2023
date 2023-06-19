# 2731. Movement of Robots

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        N = len(nums) 
        for i in range(N):
            if s[i] == "R":
                nums[i] += d
            else:
                nums[i] -= d

        nums.sort()
        result = 0
        for i in range(N):
            result += (2 * i + 1 - N) * nums[i] % (10**9 + 7) # (-1 * (N - 1 - i) + 1 * i) * nums[i]
        return result % (10**9 + 7)
