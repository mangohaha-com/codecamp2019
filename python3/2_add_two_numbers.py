# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        temp_flag = 0
        p = l1
        q = l2
        
        return_link = ListNode(0)
        temp_link = return_link
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            temp_sum = x+y+temp_flag
            temp_flag = temp_sum//10
            temp_sum %= 10

            temp_link.next = ListNode(temp_sum)
            temp_link = temp_link.next

            
            p = p.next if p else p
            q = q.next if q else q
            
        if temp_flag !=0:
            temp_link.next = ListNode(temp_flag)
            
            
        return return_link.next
            
            
            
            