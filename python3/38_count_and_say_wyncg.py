class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        init_str = '1'
        while i < n:
            init_str = self.generate(init_str)
            i += 1
        return init_str
        
        
    def generate(self, input_str):
        """
        :type str: str
        :rtype: str
        """
        temp_count = 0
        temp_char = ""
        result = ""
        for c in input_str:
            if temp_char == "":
                temp_char = c
                temp_count += 1
            else:
                if c == temp_char:
                    temp_count += 1
                else:
                    result = result + str(temp_count) + temp_char
                    temp_char = c
                    temp_count = 1
        result = result+ str(temp_count) + temp_char
        return result