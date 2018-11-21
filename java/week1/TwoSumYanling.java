class TwoSumYanling {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        //create default hashmap
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                result[0] = map.get(target - nums[i]);
                result[1] = i;
                return result;
            }
            map.put(nums[i], i);
            //Key = value of each parameter
            //Value = index
        }
        return result;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n)