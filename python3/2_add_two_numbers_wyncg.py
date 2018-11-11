# Leetcode #2
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        temp = 0
        current_node = None
        while l1 is not None or l2 is not None or temp != 0:
            current_num = 0
            n1 = 0
            n2 = 0
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            current_num = n1 + n2 + temp
            temp = current_num // 10
            current_num = current_num % 10
            if result:
                current_node.next = ListNode(current_num)
                current_node = current_node.next
            else:
                result = ListNode(current_num)
                current_node = result
        return result