#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #check x is negative or not sign equals 1 or -1
        sign=(x>0)-(x<0)
        # make num positive by times sign,conver it to str
        # slice it in reverse order then cover it to int
        num=int(str(sign*x)[::-1])
        # return sign*num or zero is sign*num out of bound
        return sign*num*(sign*num>=(-2)**21 and sign*num<2**31)
