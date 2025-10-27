from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        acc = 0
        for index, value in enumerate(nums):
            if index % 2 == 0:
                acc += value
            elif index % 2 != 0:
                acc -= value

        return acc


sol = Solution()
print(sol.alternatingSum(nums=[1, 3, 5, 7]))
