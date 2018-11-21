class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        look_up_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        prev = 0
        current = 0
        result = 0
        
        for letter in s:
            current = look_up_dict[letter]
            if current > prev:
                result += current - 2 * prev # Because prev is already added to the result
            else:
                result += current
            prev = current
        
        return result