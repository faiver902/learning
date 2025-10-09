class Solution:
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance = 0
        result = []
        temp = []

        for ch in s:
            temp.append(ch)
            if ch == "(":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                result.append("".join(temp[1:-1]))
                temp = []

        return "".join(result)


s = "(()())(())"
# s = "(()())(())(()(()))"
sol = Solution()
print(sol.removeOuterParentheses(s))
