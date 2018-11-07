class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        Important things to learn from this question:
            LCP(strs) = LCP(LCP(LCP(str1, str2), str3), str4)
            
        To summarize: compare the result with the next string
        """
        
        if len(strs) == 0:
            return ""
        
        result = strs[0]
        for i in range(1, len(strs)):
            result = self.longestCommonePrefixBetweenTwoStrings(result, strs[i])
        return result
        
    def longestCommonePrefixBetweenTwoStrings(self, str1, str2):
        min_length = min(len(str1), len(str2))
        if min_length == 0:
            return ""
        
        result = ""
        for i in range(min_length):
            if str1[i] == str2[i]:
                result += str1[i]
            else:
                return result
            
        return result