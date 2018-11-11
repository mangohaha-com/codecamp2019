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
        add_1 = False
        head = ListNode(None)
        return_list = head
        while True:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            the_sum = l1_val + l2_val + 1 if add_1 else l1_val + l2_val
            if the_sum >= 10:
                return_list.val = the_sum - 10
                add_1 = True
            else:
                return_list.val = the_sum
                add_1 = False
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2 and not add_1:
                return head
            return_list.next = ListNode(None)
            return_list = return_list.next 


        return return_list