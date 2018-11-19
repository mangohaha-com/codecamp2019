class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_length = min(len(string) for string in strs)
        results = list()
        for i in range(min_length):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return ''.join(results)
            results.append(char)
        return ''.join(results)