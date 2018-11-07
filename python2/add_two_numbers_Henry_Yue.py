# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        1. check if l1 or l2 is null
        2. if any of them is null, if one is null, result is the other one
        3. while any of the listnode has next node or carry is not zero, the loop continues
        4. In the loop, x, and y represents the current digit in each list node, then sum = x + y + carry
        5. update carry -> sum / 10
        6. update result next node to sum % 10
        7. advance to next node in l1 and l2
        """
        carry = 0
        result = temp = ListNode(0)
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            while l1 or l2 or carry:
                if l1 is None:
                    x = 0
                else:
                    x = l1.val
                    l1 = l1.next

                if l2 is None:
                    y = 0
                else:
                    y = l2.val
                    l2 = l2.next

                sum = x + y + carry
                carry = sum / 10
                temp.val = sum % 10
                
                if l1 or l2 or carry: # Check to see if it's necessay to generate next node
                    temp.next = ListNode(0)

                temp = temp.next

        return result
                
                