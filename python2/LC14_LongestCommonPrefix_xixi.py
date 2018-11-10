"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        x = ""
        if len(strs) == 0: return x
        if len(strs) == 1: return strs[0]
        
        for i in range(len(strs[0])):

            j = 1
            while j < len(strs):
                if i < len(strs[j])and strs[j][i] == strs[0][i]:
                    j += 1
                else: return x
            x = strs[0][0:i+1]

        return x