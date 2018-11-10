class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        if n == 1:
            result = "1"

        else:
            s = self.countAndSay(n - 1)
            count = 1

            for i in range(len(s)):
                num = s[i]
                if i+1 >= len(s) or s[i+1] != num:
                    result += str(count)+str(num)
                    count = 1
                else:
                    count += 1
        return result