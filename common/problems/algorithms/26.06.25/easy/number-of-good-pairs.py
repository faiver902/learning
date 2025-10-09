import collections


class Solution:
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        acc = 0

        for num in nums:
            acc += counter[num]
            counter[num] += 1
        return acc


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
