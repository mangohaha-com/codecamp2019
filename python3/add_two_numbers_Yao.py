#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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
        #initial two variable to track root and current node
        root=curr=ListNode(0)
        carry=0
        #initial loop either l1 or l2 is not None or carry is not 0
        while l1 or l2 or carry:
            # use carry to track sum of l1.val,l2.val and carry
            if l1 is not None:
                carry+=l1.val
                l1=l1.next
            if l2 is not None:
                carry+=l2.val
                l2=l2.next
            #next node val should be remain of carry divide 10
            curr.next=ListNode(carry%10)
            #update carry value
            carry=carry//10
            #point to next node
            curr=curr.next
        return root.next
             
