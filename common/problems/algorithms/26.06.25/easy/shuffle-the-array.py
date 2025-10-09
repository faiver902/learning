class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


# def shuffle(nums, n):
#     return sum(zip(nums[:n], nums[n:]), ())
