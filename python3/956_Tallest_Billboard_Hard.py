# 956. Tallest Billboard - Hard

class Solution:
    # return most highest height of mine that has differenet of diff to other's.
    def helper(self, rods: List[int], index, diff, memo) -> int:
        if (index, diff) in memo:
            return memo[(index, diff)]

        if index == len(rods) - 1:
            if diff == 0 or diff == rods[index]:
                return 0
            elif diff == -rods[index]:
                return rods[index]
            else:
                return float('-inf')

        take = self.helper(rods, index+1, diff + rods[index], memo) + rods[index]
        give = self.helper(rods, index+1, diff - rods[index], memo)
        skip = self.helper(rods, index+1, diff, memo)

        memo[(index, diff)] = max([take, give, skip])
        return memo[(index, diff)]

    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {}
        return self.helper(rods, 0, 0, memo)