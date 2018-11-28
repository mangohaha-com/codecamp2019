class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a=int(a,2)
        b=int(b,2)
        sum1=a+b
        return bin(sum1)[2:]
