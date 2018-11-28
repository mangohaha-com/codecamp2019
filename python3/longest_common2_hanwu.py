#!/bin/python3
# longest common prefix
# by hanwu

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 : return ''
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix [:-1]
        return prefix