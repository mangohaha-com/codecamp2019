#!/bin/python3
#roman to integer
#by hanwu

class Solution(object):
    def romanToInt(self, s):
        dic = {'M':1000,
                 'D':500,
                 'C':100,
                 'L':50,
                 'X':10,
                 'V':5,
                 'I':1}
        
        temp = 0
        res = 0
        for c in s:
            if dic[c] > temp:
                res -= 2 * temp
            temp = dic[c]    
            res += temp
        
        return res