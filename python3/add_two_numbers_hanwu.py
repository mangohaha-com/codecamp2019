#!/bin/python3
#add two numbers
#by hanwu

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        remain = 0
        l = ListNode(None)
        result = l
        
        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
            total = l1.val + l2.val + remain
            if total >=10 :
                total = total - 10
                remain =1
            else:
                remain = 0
            l.next = ListNode(total)
            l1 = l1.next
            l2 = l2.next
            l = l.next
            
        if remain == 1:
            l.next = ListNode(remain)
            
        return result.next