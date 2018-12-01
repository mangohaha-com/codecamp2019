class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        maxvalue = minvalue = nums[0]
        globalmax = nums[0]
        for i in range(1, len(nums)):
            lastmax = maxvalue
            lastmin = minvalue
            maxvalue = max(lastmin * nums[i], lastmax * nums[i], nums[i])
            minvalue = min(lastmin * nums[i], lastmax * nums[i], nums[i])
            globalmax = max(globalmax, maxvalue)
        return globalmax
        
        #本题要求连续子数组的最大乘积，思路与求连续子数组的最大和相似，都是采用动态规划，
        maxvalue[i]maxvalue[i]表示以a[i]a[i]为结尾的子数组中最大乘积，
        同时维护一个全局最大值globalmaxglobalmax，
        记录maxvalue[i]maxvalue[i]中的最大值。
        与求子数组的最大和不同的是，还需要维记录子数组最小乘积minvalue[i]minvalue[i]，
        因为可能会出现 负 × 负 = 正的情况。
        并且最大最小乘积只可能出现在 (maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])(maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])三者之间。
