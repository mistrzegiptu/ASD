class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertionSortList(self, head):
        current = head
        tail = head
        current = current.next

        while current:
            if tail.val > current.val:
                temp = current
                tail.next = current.next
                current = current.next
                temp.next = None
                head = self.insertSorted(Solution, head, temp)
            else:
                tail = tail.next
                current = current.next

        return head

    def insertSorted(self, head, node):
        current = head
        if not head or not node:
            return node
        if head.val > node.val:
            node.next = head
            return node

        while current.next:
            if current.next.val > node.val:
                node.next = current.next
                current.next = node
                return head
            current = current.next

        current.next = node
        return head


h = ListNode(10)
h.next = ListNode(8)
h.next.next = ListNode(4)
h.next.next.next = ListNode(9)

h = Solution.insertionSortList(Solution, h)

while h:
    print(h.val)
    h = h.next