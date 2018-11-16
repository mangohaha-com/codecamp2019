class Solution(object):
    """
    A better explanation of the problem is written here:
    https://oeis.org/A005150
    """

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2:
            return "1"
        else:
            string_to_count = self.countAndSay(n - 1)
            result = ""
            repeat = string_to_count[0]
            counts = 1
            
            for i in range(len(string_to_count) - 1):
                
                if string_to_count[i + 1] != repeat:
                    result += str(counts) + repeat
                    counts = 1
                    repeat = string_to_count[i + 1]
                else:
                    counts += 1
            result += str(counts) + repeat # Taking care of the last digit
            
            return result