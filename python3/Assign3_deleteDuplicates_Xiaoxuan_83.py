class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = head
        while l and l.next:
            if l.next.val == l.val:
                l.next = l.next.next
            else:
                l = l.next
        return head