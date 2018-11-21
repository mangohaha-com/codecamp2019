# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Loop invariant: All nodes in the list up to the pointer current do not contain duplicate elements.
        """
        if not head: return head
        
        current = head
        
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head