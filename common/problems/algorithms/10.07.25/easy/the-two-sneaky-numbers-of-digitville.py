from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        result = []
        for key, value in counter.items():
            if value == 2:
                result.append(key)
        return result


s = Solution()
print(s.getSneakyNumbers([0, 1, 1, 0]))
