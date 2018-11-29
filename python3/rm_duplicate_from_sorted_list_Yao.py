#!/usr/bin/env python3
# -*- coding:utf-8 -*-
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
        curr=head # give a mark for head
        while curr and curr.next: 
            if curr.val==curr.next.val: # keep update curr.next if val is duplicate
                curr.next =curr.next.next
            else:
                curr=curr.next        # update curr if not duplicate
        return head
            
