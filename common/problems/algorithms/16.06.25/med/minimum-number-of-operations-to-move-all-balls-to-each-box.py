class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        result = [0] * n

        # Слева направо
        count = 0  # сколько шаров уже было
        ops = 0  # сколько операций накопилось
        for i in range(n):
            result[i] += ops
            if boxes[i] == "1":
                count += 1
            ops += count

        # Справа налево
        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            result[i] += ops
            if boxes[i] == "1":
                count += 1
            ops += count

        return result


s = Solution()
boxes = "001011"

print(s.minOperations(boxes))
