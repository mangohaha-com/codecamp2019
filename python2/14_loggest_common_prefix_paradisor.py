class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #res = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            for i in range(min(len(s) for s in strs)):
                if not all(s[i] == strs[0][i] for s in strs):
                    return strs[0][:i]
                       #res = res + strs[0][i]
                #else:
                       #return res
            return min(strs, key=len)
        #return ""#res