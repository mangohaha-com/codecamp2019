class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        we get the minimum of adjacent group and add them together
        """
        count = 0
        previous = ""
        currentContinousCount = 0
        currentContinousCountLeft = 0
        counting = False
        for char in s:
            # first char
            if previous == "":
                previous = char
                currentContinousCount += 1
                continue
            # current char is equal to previous, increase current continous count
            # if we are counting, minus the continous count left so we know when to stop
            if char == previous:
                currentContinousCount += 1
                if counting:
                    currentContinousCountLeft -= 1
                    if currentContinousCountLeft >= 0:
                        count += 1
                    else:
                        counting = False
                continue
            # group switch, we need to start count
            if char != previous:
                currentContinousCountLeft = currentContinousCount - 1
                currentContinousCount = 1
                counting = True
                count += 1
                previous = char
                continue
                
        return count
    
        """
        groups = [1]
        # build groups array
        for i in range(1, len(s)):
            if s[i-1] == s:
                groups[-1] += 1
            else:
                groups.append(1)
                
        count = 0
        for i in range(1, len(groups)):
            count += min(groups[i-1], groups[i])
            
        return count
        """