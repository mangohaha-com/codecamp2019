class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        for char in t:
            if s == "":
                return char
            dup = s.replace(char, "", 1)
            
            if len(s) == len(dup):
                return char
            s = dup
        """

        #use set
        setT = set(t)
        for char in setT:
            if t.count(char) != s.count(char):
                return char