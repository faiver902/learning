class Solution:
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc = 0
        for i in nums:
            if i < k:
                acc += 1
        return acc


nums = [1, 1, 2, 4, 9]
k = 1
sol = Solution()
print(sol.minOperations(nums, k))
