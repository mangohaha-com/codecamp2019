class RemoveElement27 {
    public int removeElement(int[] nums, int val) {
        if(nums == null || nums.length == 0) return -1;
        int count = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != val) {
                if(i != count) {
                    int tmp = nums[i];
                    nums[i] = nums[count];
                    nums[count] = tmp;
                }
                count++;
            }
        }
        return count;
    }
}