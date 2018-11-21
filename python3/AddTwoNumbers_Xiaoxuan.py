class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getn(ln):
            tn, count, sum = ln, 0, 0
            while tn != None:
                sum += tn.val * 10 ** count
                count += 1
                tn = tn.next
            return sum
        total = list(str(getn(l1)+getn(l2)))
        return [ int(x) for x in total[::-1] ]






