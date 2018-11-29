#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                num-=dic[s[i]]
            else:
                num+=dic[s[i]]
        return num+dic[s[-1]]
