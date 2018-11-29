#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=x
        while r*r > x:
            r= int((r+x/r)//2) # Newton's Method
        return r

