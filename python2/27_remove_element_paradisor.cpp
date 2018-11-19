class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size()==0) return 0;
        int dup = 0;
        int pos = 0;
        while (pos < nums.size()){
            if (pos == dup && nums[dup] != val){
                dup++;
                pos++;
            }
            else if (nums[pos] == val){
                pos++;
            } else {
                swap(nums[pos], nums[dup]);
                dup++;
            }
        }
        return dup;
    }
};