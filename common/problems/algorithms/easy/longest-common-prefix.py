class Solution:
    def longestCommonPrefix(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        i = 0
        for column in zip(*strs, strict=False):
            if len(set(column)) == 1:
                i += 1
            else:
                break

        return strs[0][:i]

    def longestCommonPrefix2(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        a, b = min(strs), max(strs)

        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1

        return a[:i]


strs = ["flower", "flow", "flight"]
s = Solution()
print(s.longestCommonPrefix2(strs))
