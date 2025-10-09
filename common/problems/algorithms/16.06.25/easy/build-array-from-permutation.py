class Solution:
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        return [nums[nums[i]] for i in range(len(nums))]
        """
        return [nums[nums[i]] for i in range(len(nums))]


s = Solution()
s.buildArray([0, 2, 1, 5, 3, 4])
