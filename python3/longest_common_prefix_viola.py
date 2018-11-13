"""
week 2

code has passed on leetcode.com
"""
class Solution:
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        comm = strs[0]
        for i in range(len(strs) - 1):
            sidx = i + 1
            for w in range(len(strs[sidx])):
                if w >= len(comm):
                    comm = comm[0:w-1]
                    break
                if not comm[w] == strs[sidx][w]:
                    if w == 0:
                        comm = ""
                    comm = comm[0:w]
                    continue
        return comm
