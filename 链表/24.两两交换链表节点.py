from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归法
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = head
        cur = head.next
        next = head.next.next

        cur.next = prev
        prev.next = self.swapPairs(next)

        return cur

    # 循环法
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head

        while cur.next and cur.next.next:
            tmp = cur.next
            tmp2 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = tmp2
            cur = cur.next.next
        return dummy_head.next
