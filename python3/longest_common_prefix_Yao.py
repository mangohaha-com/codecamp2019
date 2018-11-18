class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
      
        for i, group in enumerate(zip(*strs)):
            if len(set(group))>1:
                return strs[0][:i]
    
        return min(strs)
