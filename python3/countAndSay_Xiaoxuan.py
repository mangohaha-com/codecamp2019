class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        times = 1
        seq = '1'
        while times < n:
            new_seq = ''
            count = 0
            for i in range(len(seq)):
                count += 1
                if i == len(seq)-1:
                    new_seq += str(count)
                    new_seq += seq[i]
                elif seq[i] != seq[i+1]:
                    new_seq += str(count)
                    new_seq += seq[i]
                    count = 0

            seq = new_seq
            times += 1
        return seq











