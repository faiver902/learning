class Solution:
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        result = []
        for o in order:
            if o in friends:
                result.append(o)
        return result


order = [3, 1, 2, 5, 4]
friends = [1, 3, 4]

sol = Solution()
print(sol.recoverOrder(order, friends))
