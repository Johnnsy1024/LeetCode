class ListNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int):
        self.head = ListNode(val, self.head)
        self.size += 1

    def addAtTail(self, val: int):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int):
        if index <= 0:
            self.addAtHead(val)
        elif index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = ListNode(val)
            cur_node = self.head
            for i in range(index - 1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur_node = self.head
            for i in range(index - 1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
        self.size -= 1


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(2)
