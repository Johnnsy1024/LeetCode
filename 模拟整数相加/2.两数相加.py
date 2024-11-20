# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """和415字符串相加类,只是把字符串按位相加变成了链表节点挨个相加,值得注意的点是当前节点在向前移动时,需要判断是否需要创建新的节点,也就是判断是否是最后一次相加,最后一次相加的条件是d1,d2,carry都为0,否则需要创建新的节点,否则会报错,

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        d1 = l1
        d2 = l2
        carry = 0
        head = ListNode()
        cur_node = head
        while d1 or d2 or carry > 0:
            if d1:
                temp1 = d1.val
                d1 = d1.next if d1.next else None
            else:
                temp1 = 0
            if d2:
                temp2 = d2.val
                d2 = d2.next if d2.next else None
            else:
                temp2 = 0
            cur_node.val = (temp1 + temp2 + carry) % 10
            carry = (temp1 + temp2 + carry) // 10
            if not d1 and not d2 and not carry:
                cur_node.next = None
            else:
                cur_node.next = ListNode()
            cur_node = cur_node.next
        return head
