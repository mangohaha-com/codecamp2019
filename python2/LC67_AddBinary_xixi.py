class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        add = 0
        la = len(a) - 1
        lb = len(b) - 1
        s = ""
        
        while i <= max(la, lb):
            na = 0
            nb = 0
            if i <= la: na = int(a[la - i])                
            if i <= lb: nb = int(b[lb - i])                
            s += str((na + nb + add) % 2)
            add = (na + nb + add) / 2
            i += 1

        if add > 0:
            s += str(add)

        return s[::-1] 