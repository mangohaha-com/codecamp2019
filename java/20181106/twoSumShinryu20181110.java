class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> tempMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i ++){
            if (tempMap.containsKey(target - nums[i])){
                return new int[] {tempMap.get(target - nums [i])};
            }
            tempMap.put(nums[i], i);
        }
        throw new IllegalArgumentException("No pairs found");
    }
}