class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" or haystack == needle:
            return 0
        if haystack == "" or len(needle) >= len(haystack):
            return -1 
        for i in range(len(haystack)):
            if i > len(haystack) - len(needle):
                return -1
            not_match = False
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    not_match = True
                    break
            if not not_match:
                return i
        return -1