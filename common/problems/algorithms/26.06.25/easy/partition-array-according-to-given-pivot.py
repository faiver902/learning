class Solution:
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        low, mid, high = [], [], []

        for i in nums:
            if i > pivot:
                high.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                low.append(i)
        return low + mid + high
