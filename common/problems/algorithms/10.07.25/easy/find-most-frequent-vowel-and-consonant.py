from collections import Counter


class Solution:
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        w = "a,e,i,o,u"
        vowels = [value for key, value in counter.items() if key in w]
        consonants = [value for key, value in counter.items() if key not in w]

        temp_w_count = max(vowels, default=0)
        temp_c_count = max(consonants, default=0)

        return temp_w_count + temp_c_count


s = Solution()
print(s.maxFreqSum("aeiaeia"))
