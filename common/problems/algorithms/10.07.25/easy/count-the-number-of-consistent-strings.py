class Solution:
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        def filt(w):
            for l in w:
                if l not in allowed:
                    return
            return w

        return len(list(filter(filt, words)))


s = Solution()
print(s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
