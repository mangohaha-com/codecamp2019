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
        fullList = ListNode(0)
        tempList = fullList
        tempNum = None
        while head:
            if tempNum == head.val and tempNum is not None:
                head = head.next
                continue

            tempNum = head.val
            tempList.next = head
            tempList = tempList.next
            head = head.next
        
        if tempList.next and tempList.val == tempList.next.val:
            tempList.next = None
        return fullList.next