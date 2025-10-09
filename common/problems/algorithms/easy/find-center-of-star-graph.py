class Solution:
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[0][0] == edges[1][0] or edges[1][1] == edges[0][0]:
            return edges[0][0]
        else:
            return edges[0][1]


s = Solution()
edges = [[1, 2], [2, 3], [4, 2]]
print(s.findCenter(edges))
