from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return self.recursion(head, None)

    def recursion(
        self,
        cur: Optional[ListNode],
        prev: Optional[ListNode],
    ) -> Optional[ListNode]:
        """递归法翻转链表
        注意,递归翻转链表时,必须要传递prev节点
        Args:
            cur (Optional[ListNode]): 当前节点
            prev (Optional[ListNode]): 前节点

        Returns:
            Optional[ListNode]: _description_
        """
        if not cur:
            return prev
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
        return self.recursion(cur, prev)


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    res = s.reverseList2(head)
    pass
