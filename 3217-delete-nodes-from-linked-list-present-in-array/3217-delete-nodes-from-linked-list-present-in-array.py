
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values = set(nums)
        while head is not None and head.val in values:
            head = head.next

        current = head
        while current is not None and current.next is not None:
            if current.next.val in values:
                current.next = current.next.next
            else:
                current = current.next

        return head