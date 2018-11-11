class Solution:
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    original_length = len(nums)
    while i < original_length:
      first_element = nums.pop(0)
      if first_element != val:
        nums.append(first_element)
      i+=1
    return len(nums)