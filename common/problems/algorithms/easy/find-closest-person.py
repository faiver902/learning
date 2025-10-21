class Solution:
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if abs(z - x) < abs(z - y):
            return 1
        elif abs(z - y) < abs(z - x):
            return 2
        else:
            return 0


x = 2
y = 7
z = 4
sol = Solution()
print(sol.findClosest(x, y, z))
