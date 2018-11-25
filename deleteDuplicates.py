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
        if head == None:
            return head
        list1 = []
        while head:
            if head.val not in list1:
                list1.append(head.val)
            head = head.next
        return list1
        # if head == None:
        #     return head
        # current = head.next
        # prev = head
        # while current:
        #     if current.val == prev.val:
        #         prev.next = current.next
        #         current = current.next
        #     else:
        #         prev = prev.next
        #         current = current.next
        # return head
