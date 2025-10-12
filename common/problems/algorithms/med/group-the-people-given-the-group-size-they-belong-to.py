from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """ """
        mapping = defaultdict(list)
        result = []
        for index, group_size in enumerate(groupSizes):
            mapping[group_size].append(index)

            if len(mapping[group_size]) == group_size:
                result.append(mapping[group_size])
                mapping[group_size] = []

        return result


groupSizes = [3, 3, 3, 3, 3, 1, 1, 3]
s = Solution()
print(s.groupThePeople(groupSizes))
