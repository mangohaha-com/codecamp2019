class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        a=0
        for i in range (len(s)-1):
            if dict[s[i]]<dict[s[i+1]]:
                a-=dict[s[i]]
            else:
                a+=dict[s[i]]
                
        return a+dict[s[-1]]
