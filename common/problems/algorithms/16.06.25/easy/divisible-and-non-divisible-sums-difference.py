class Solution:
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num_2 = sum([i for i in range(n + 1) if i % m == 0])
        num_1 = sum([i for i in range(n + 1) if i % m != 0])

        return num_1 - num_2


s = Solution()
s.differenceOfSums(10, 3)
li = [1, 2, 3]
