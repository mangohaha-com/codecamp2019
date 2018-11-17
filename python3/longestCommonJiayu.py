class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """     
      
        if not strs:
      
    return ""
        t=''
        for i in range (len(strs[0])):
            for j in range (1, len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=strs[0][i]:
                        return t
            t+=strs[0][i]
        return t
