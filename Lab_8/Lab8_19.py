class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = prev.next.next
        return dummy.next