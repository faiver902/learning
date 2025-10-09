class Solution:
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return sum([abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)])
        result = 0
        for i in range(len(s) - 1):
            result += abs(ord(s[i]) - ord(s[i + 1]))

        return result


s = Solution()
s.scoreOfString("hello")
