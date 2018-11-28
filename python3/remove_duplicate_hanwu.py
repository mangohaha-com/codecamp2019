#!/bin/python3
#Remove Duplicates from Sorted List
#by hanwu

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_list = []
        while head!= None:
            if head.val not in my_list:
                my_list += [head.val]
            head = head.next
        return my_list