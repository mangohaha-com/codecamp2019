# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        index=head
        point=head.next
        while point is not None:
            if point.val!=index.val:
                index.next,index=point,point
            else:
                index.next=None
            point=point.next
        return head
        
