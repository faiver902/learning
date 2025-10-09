from collections import Counter


class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        need_divisors = Counter([num * k for num in nums2])
        print(need_divisors)
        result = 0
        for i in nums1:
            for o in nums2:
                if i % (o * k) == 0:
                    result += 1

        return result


Counter()
nums1 = [1, 2, 4, 12]
nums2 = [2, 4]
k = 3

sol = Solution()
print(sol.numberOfPairs(nums1, nums2, k))
