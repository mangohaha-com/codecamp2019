#!/bin/python3
#add binary
#by hanwu

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = bin(int(a,2) + int(b,2))
        return c[2:]