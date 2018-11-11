Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def TwoSum(nums, target):
    res = {}
    for i in range(len(nums)):
        if nums[i] not in res:
            res[nums[i]] = i
        if (target - nums[i]) in res:
            return [res[target - nums[i]], i]
