class Solution:
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        map_s = {v: index for index, v in enumerate(s)}
        map_t = {v: index for index, v in enumerate(t)}

        acc = 0
        for key in map_s:
            acc += abs(int(map_s[key]) - int(map_t[key]))
        return acc


s = "abcde"
t = "edbac"

sol = Solution()
print(sol.findPermutationDifference(s, t))
