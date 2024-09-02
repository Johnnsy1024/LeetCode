class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    这里的相交节点指的是两个地址相同的节点,而不是两个值相同的节点
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """如果两个链表存在相交的位置,则相交部分一定是两个链表各自的尾部,也就是说,两个链表的尾部一定是对齐的.因此,先把两个链表从尾部对齐,然后分别用一个指针指向较长链表与较短链表的对齐的位置,另一个指针指向较短链表的头部,同时移动两个指针,当两个指针指向的节点相等(指向的对象相同而不是值相同)时,返回该节点,否则返回空

        Args:
            headA (ListNode): _description_
            headB (ListNode): _description_

        Returns:
            ListNode: _description_
        """
        # 如果两个头节点都为空,则直接返回空
        if (not headA) or (not headB):
            return None
        cur_A = headA
        len_A, len_B = 1, 1
        while cur_A:
            cur_A = cur_A.next
            len_A += 1
        cur_B = headB
        while cur_B:
            cur_B = cur_B.next
            len_B += 1
        idx = abs(len_A - len_B)
        if len_A > len_B:
            cur_A = headA
            for _ in range(idx):
                cur_A = cur_A.next
            cur_B = headB
            while cur_B:
                if cur_B == cur_A:
                    return cur_A
                else:
                    cur_A = cur_A.next
                    cur_B = cur_B.next
        else:
            cur_B = headB
            for _ in range(idx):
                cur_B = cur_B.next
            cur_A = headA
            while cur_A:
                if cur_A == cur_B:
                    return cur_B
                else:
                    cur_A = cur_A.next
                    cur_B = cur_B.next
        return None
