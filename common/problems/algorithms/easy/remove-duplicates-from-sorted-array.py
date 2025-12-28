from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        acc = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[acc]:
                acc += 1
                nums[acc] = nums[i]
        return len(set(nums))

s = Solution()
print(s.removeDuplicates([1,1,2]))