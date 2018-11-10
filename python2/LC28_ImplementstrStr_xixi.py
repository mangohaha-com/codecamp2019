"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        index = -1
        
        for i in range(len(haystack)-len(needle)+1):
            
            if len(needle) == 0: index = 0
            elif haystack[i:i+len(needle)] == needle:
                index = i
                break
        
        
        return index