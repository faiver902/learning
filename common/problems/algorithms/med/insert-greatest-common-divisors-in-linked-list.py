# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import math


class Solution:
    def insertGreatestCommonDivisors(self, head):
        """
        Вставляет между каждым pair соседних узлов новый узел со значением НОД.
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1) Пустой список или один элемент — ничего не делаем
        if not head or not head.next:
            return head

        curr = head
        # 2) Идём, пока есть пара curr и curr.next
        while curr and curr.next:
            nxt = curr.next  # не теряем ссылку = nxt=10
            g = math.gcd(curr.val, nxt.val)  # вычисляем НОД = g=2
            new_node = ListNode(g, nxt)  # вставляем между curr и nxt = new_node=2, ->10
            curr.next = new_node  # curr.next = 10

            curr = nxt  # 3) идём дальше к исходному следующему (перешагиваем через вставленный) curr=None
        return head


# Вспомогательные функции для локальных проверок (вне LeetCode)
def build_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# Пример:
head = build_list([18, 6, 10])
res = Solution().insertGreatestCommonDivisors(head)
print(to_list(res))  # [18, 6, 6, 2, 10]
