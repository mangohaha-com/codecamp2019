class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lut = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in lut.keys():
                return [lut[diff],i]
            else:
                lut[numbers[i]] = i

        return [-1,-1]