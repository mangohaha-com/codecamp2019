"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        pointer = dummy
        carry_in = 0

        while l1 is not None and l2 is not None:
            result = l1.val + l2.val + carry_in

            pointer.next = ListNode(result%10)
            carry_in = result / 10

            l1 = l1.next
            l2 = l2.next
            pointer = pointer.next

        while l1 is not None:
            result = l1.val + carry_in
            pointer.next = ListNode(result%10)
            carry_in = result / 10
            l1 = l1.next
            pointer = pointer.next

        while l2 is not None:
            result = l2.val + carry_in
            pointer.next = ListNode(result%10)
            carry_in = result/10
            l2 = l2.next
            pointer = pointer.next

        if carry_in == 1:
            pointer.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)

    l2 = ListNode(9)

    sol = Solution()
    result = sol.addLists(l1,l2)

    while result is not None:
        print(result.val)
        result = result.next