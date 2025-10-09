# class Solution(object):
#     def pivotArray(self, nums, pivot):
#         """
#         https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
#         :type nums: List[int]
#         :type pivot: int
#         :rtype: List[int]
#         """
#         result = []
#         len_nums = len(nums)
#         mid_len = len_nums // 2
#
#         for index, value in enumerate(nums):
#             if value > pivot:
#                 result.insert(mid_len + 1, value)
#             elif value < pivot:
#                 result.insert(mid_len - 1, value)
#             else:
#                 result.insert(mid_len - 1, value)
#         return result
#
#
# s = Solution()
#
# nums = [9, 12, 5, 10, 14, 3, 10]
# pivot = 10
# print(s.pivotArray(nums, pivot))
