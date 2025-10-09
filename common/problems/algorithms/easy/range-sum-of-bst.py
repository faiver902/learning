# ==== Определение узла дерева ====
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==== Построение дерева по списку level-order (LeetCode-формат) ====
from collections import deque


def build_tree_level_order(values):
    """
    Преобразует список вида [10,5,15,3,7,None,18] в бинарное дерево.
    values[i] = None означает отсутствие соответствующего узла.
    Возвращает корень (TreeNode) или None.
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i, n = 1, len(values)

    while q and i < n:
        node = q.popleft()

        # Левый ребёнок
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        # Правый ребёнок
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root


# ==== Решение задачи 938. Range Sum of BST ====
class Solution:
    def rangeSumBST(self, root, low, high):
        """
        Возвращает сумму значений в диапазоне [low, high] включительно.
        Используем свойство BST для отсечения ветвей.
        """
        if root is None:
            return 0

        if root.val < low:
            # всё левое поддерево < low — идём только вправо
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            # всё правое поддерево > high — идём только влево
            return self.rangeSumBST(root.left, low, high)

        # узел в диапазоне — учитываем и идём в обе стороны
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )


# ==== Тест ====
if __name__ == "__main__":
    arr = [10, 5, 15, 3, 7, None, 18]
    low, high = 7, 15
    root = build_tree_level_order(arr)  # тут получаем корень дерева (TreeNode)
    s = Solution()
    print(s.rangeSumBST(root, low, high))  # ожидаем 32
