from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        acc = 0
        for num in nums:
            if num % 3 != 0:
                acc += 1
        return acc


sol = Solution()
print(sol.minimumOperations(nums=[1, 2, 3, 4]))
