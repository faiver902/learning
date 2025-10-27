from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ = sum(nums)
        acc = 0
        while summ % k != 0:
            acc += 1
            summ -= 1

        return acc


sol = Solution()
print(sol.minOperations(nums=[3, 2], k=6))
