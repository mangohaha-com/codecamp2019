class Solution {
  public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0){
    return "";
    }
    String ans = new String();
    for (int i = 0; i < strs[0].length(); ++i) {
      char c = strs[0].charAt(i);
      for (String s : strs)
        if (s.length() <= i || s.charAt(i) != c){
        return ans;
        }
        ans += c;
    }
    return ans;
  }
}
