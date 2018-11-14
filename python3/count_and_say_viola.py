"""
week 2

code has passed on leetcode.com
"""
class Solution:
    def countnum(self, n):
        tmp = ""
        count = 1
        word = []
        num = []
        for i in n:
            if tmp == i:
                count += 1
            else:
                if tmp == "":
                    tmp = i
                    continue
                num.append(count)
                word.append(tmp)
                count = 1
            tmp = i
        num.append(count)
        word.append(tmp)
        
        return num, word
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = "1"
        for _ in range(n - 1):
            rst = ""
            num, word = self.countnum(say)
            for nu, wd in zip(num, word):
                rst += str(nu)
                rst += wd
            say = rst
        
        return say
            
            
