
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast == None:
            head = head.next
            return head

        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
