class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldStr = '1'
        for i in range(n-1):
            tmp = ''
            for j in range(1, len(oldStr) + 1):
                if j < len(oldStr) and oldStr[j] == oldStr[j - 1]:
                    count += 1
                else:
                    tmp += str(count) + oldStr[j - 1]
                    count = 1
            oldStr = tmp 
        return oldStr
    #time:O(n)
    #Space: O(1)
