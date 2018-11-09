"""
Week2 11/14 Due
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        add = 0
        current1 = l1
        current2 = l2
     
        l3 = ListNode(0) # dummy head
        current3 = l3
     

        while current1 and current2:

            current3.next = ListNode((current1.val + current2.val + add ) % 10)
            add = (current1.val + current2.val + add) / 10

            current1 = current1.next
            current2 = current2.next
            current3 = current3.next

        while current1:
            current3.next = ListNode((current1.val + add) % 10)
            add = (current1.val +add) / 10

            current1 = current1.next
            current3 = current3.next

        while current2:
            current3.next = ListNode((current2.val + add) % 10)
            add = (current2.val+add) / 10

            current2 = current2.next
            current3 = current3.next



        if add: current3.next = ListNode(add)


        return l3.next
            
        