class Solution:
    def longestCommonPrefix(self, strs):
        if strs == [] or "" in strs:
            return ""
        else:
            minstr = min(strs, key=len)
            end = 1
            for i in range(len(minstr)):
                shortest = minstr[0:i+1]
                count = 0
                for i_str in strs:
                    if i_str[0:i+1] == shortest:
                        count += 1
                if count == len(strs):
                    end += 1
                else:
                    end = i
                    break
            return minstr[0:end]







