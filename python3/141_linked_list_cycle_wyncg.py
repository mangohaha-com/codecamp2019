# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        hash table
        do not use array. it's slower than set and got time limit exceeded
        """
        current = head
        sets = set()
        if not current:
            return False
        while current not in sets:
            sets.add(current)
            if current.next is None:
                return False
            current = current.next
        return True
        
        """
        two pointers
        
        # check if empty or None
        if not head:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
        """