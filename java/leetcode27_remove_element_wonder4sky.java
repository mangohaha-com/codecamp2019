class Solution {
    public int removeElement(int[] nums, int val) {
        // 逆向思维： 要求删掉，那么如何把不删除的写上呢（赞）
        int begin = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[begin++] = nums[i];
            }
        }
        return begin;
    }
}



/**如果不考虑空间，用hashmap怎么做呢
 int len = nums.length;
 int val = 0
 HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

 for (int i = 0; i < len; i++) {
 if (!map.containsKey(nums[i]))
 map.put(nums[i], 1);
 else
 map.put(nums[i], (map.get(nums[i]) + 1));
 }**/
        
