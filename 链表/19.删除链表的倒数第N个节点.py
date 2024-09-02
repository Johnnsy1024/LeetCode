# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow和fast指针都指向虚拟节点
        dummy_node = ListNode(-1)
        dummy_node.next = head
        # fast指针先走n+1步
        # 然后slow指针跟随fast指针一直走到fast为null
        fast = dummy_node
        slow = dummy_node
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    print(Solution().removeNthFromEnd(head, 1))
