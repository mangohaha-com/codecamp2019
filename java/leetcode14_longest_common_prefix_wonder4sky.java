class Solution {
    public String longestCommonPrefix(String[] strs) {


        /**String str = "";
         if (strs.length == 0) return str;
         int j = 1;
         for (int i = 0; i < strs[0].length(); i++) {
         for (j = 1; j < strs.length; j++) {
         if (i >= strs[j].length())
         return str;
         else if (strs[j].charAt(i) == strs[0].charAt(i))
         continue;
         else
         return str;
         }
         str = str + strs[0].charAt(i);
         }
         return str;
         }**/
        String str = "";

        if (strs == null || strs.length == 0) return str;
        int j;
        int min = strs[0].length();
        for (j = 0; j< strs.length; j++) {
            //int min = strs[0].length();
            if (strs[j].length() < min)
                min = strs[j].length();
        }

        for (int i = 0; i < min; i++) {
            for (j = 1; j < strs.length; j++) {
                if (i >= strs[j].length())
                    return str;
                else if (strs[j].charAt(i) == strs[0].charAt(i))
                    continue;
                else
                    return str;
            }
            str = str + strs[0].charAt(i);
        }
        return str;
    }
}
