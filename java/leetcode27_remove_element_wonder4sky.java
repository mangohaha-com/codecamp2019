class Solution {
    public int removeElement(int[] nums, int val) {
        // ????? ????????????????????
        int begin = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[begin++] = nums[i];
            }
        }
        return begin;
    }
}

        
        
        /**?????????hashmap????
        int len = nums.length;
        int val = 0
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < len; i++) {
            if (!map.containsKey(nums[i]))
                map.put(nums[i], 1);
            else 
                map.put(nums[i], (map.get(nums[i]) + 1));
        }**/
        
