//Time complexity: O(m*n), m is the length of the first string, while n is the string array length
//Space complexity; O(m), where m is the length of the result string.
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0) return "";
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < strs[0].length(); i++) {
            char cur = strs[0].charAt(i);
            int j = 0;
            for(; j < strs.length && i < strs[j].length(); j++) {
                if(strs[j].charAt(i) != cur) {
                    break;
                }
            }
            if(j == strs.length){
                sb.append(cur);
            } else {
                return sb.toString();
            }
        }
        return strs[0];
    }
}