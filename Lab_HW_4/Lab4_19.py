class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_prog = ListNode(0)
        head_prog.next = head
        fast = head_prog
        slow = head_prog
        for _ in range(n):
            fast = fast.next
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = prev.next.next
        return head_prog.next