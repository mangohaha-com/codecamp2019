class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """
        recursive:
        if a == "":
            return b
        if b == "":
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        """
        result = ""
        carry = "0"
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        while shorter != "":
            current_longer = longer[-1]
            current_shorter = shorter[-1]
            longer = longer[:-1]
            shorter = shorter[:-1]
            if int(current_longer) + int(current_shorter) + int(carry) == 0:
                result = '0' + result
                carry = '0'
            elif int(current_longer) + int(current_shorter) + int(carry) == 1:
                result = '1' + result
                carry = '0'
            elif int(current_longer) + int(current_shorter) + int(carry) == 2:
                result = '0' + result
                carry = '1'
            else:
                result = '1' + result
                carry = '1'
        while longer != "":
            current = longer[-1]
            longer = longer[:-1]
            if int(current) + int(carry) == 0:
                result = '0' + result
                carry = '0'
            elif int(current) + int(carry) == 1:
                result = '1' + result
                carry = '0'
            else:
                result = '0' + result
                carry = '1'

        if carry == '1':
            return carry + result
        else:
            if result[0] == '0' and result != '0':
                return result[1:]
        return result