class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([bin(int(i))[2:] for i in date.split("-")])


date = "2080-02-29"
sol = Solution()
print(sol.convertDateToBinary(date))
