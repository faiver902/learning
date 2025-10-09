class Solution:
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = self.create_mapping_char()
        acc = 0
        for index, char in enumerate(s):
            acc += mapping[char] * (index + 1)

        return acc

    @staticmethod
    def create_mapping_char():
        mapping = {}
        step = 26
        for i in range(97, 123):
            mapping[chr(i)] = step
            step -= 1
        return mapping


s = "zaza"
sol = Solution()
print(sol.reverseDegree(s))
