//Time complexity: O(n)
//Space Complexity: O(1)

public class RemoveElementGuangting {
    public int removeElement(int[] nums, int val) {
        if(nums == null || nums.length == 0) return 0;
        int len = nums.length;
        int j = len - 1;
        for(int i = len - 1; i >= 0;) {
            while(i >= 0 && nums[i] == val) {
                i--;
            }
            if(i >= 0) {
                nums[j--] = nums[i--];
            } else {
                break;
            }
        }
        int res = len - j - 1;
        for(int i = 0; i < res && j + 1 < len; i++) {
            nums[i] = nums[++j];
        }
        return res;
    }
}
