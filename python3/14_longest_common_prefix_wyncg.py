class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        str = strs[0]
        for i in range(len(strs)):
            if i == 0:
                continue
            while str != strs[i][:len(str)]:
                str = str[:-1]
                if str == "":
                    return ""
        return str