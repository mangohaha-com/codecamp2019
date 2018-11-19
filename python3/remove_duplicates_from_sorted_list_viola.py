"""
week 3

code has passed on leetcode.com
"""

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
        
        slist = head
        if head == None:
            return head
        while not slist.next == None:
            if not slist.val == slist.next.val:
                slist = slist.next
            else:
                slist.next = slist.next.next
                
        return head
