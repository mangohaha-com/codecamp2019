class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        #When you slice the string like haystack here for example, 
        you're creating a copy of the string. Sure it's only the size of needle,
        but just wanted to point out. 
        The string comparison is O(n) where n is size of needle so solution is O(n * h) at best where h is size of haystack.
