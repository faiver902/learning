class Solution:
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l1 = [1 for value in nums if value % 2 != 0]
        l2 = [0 for value in nums if value % 2 == 0]
        return sorted(l1 + l2)
