class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=""
        if n ==1:
            return "1"
        elif n > 1:
            s=self.countAndSay(n-1)
            i=j=0
            while (j <len(s)) and (i<len(s)):
                if s[i]==s[j]:
                    j+=1
                
                elif s[i] != s[j]:
                    res+=str(j-i) + s[i]
                    i=j
            res+=str(j-i)+s[i]
        return res
