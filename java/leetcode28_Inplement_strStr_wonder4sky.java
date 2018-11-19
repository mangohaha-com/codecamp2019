class Solution {
    public int strStr(String haystack, String needle) {
        //???? ?substring();??substring()??????????????
        int len = needle.length();
        for (int i = 0; i< haystack.length() - len + 1; i++) {
            if(haystack.substring(i, i+len).equals(needle))
                return i;
        }
        return -1;
    }
}
        
        
        //????????????????????
        /**char[] charsH = haystack.toCharArray();
        int index = 0;
        for (int i = 0; i < needle.length(); i++) {
            for (int j = 0; j < charsH.length; j++) {
                if (charsH[j] != needle.charAt(i)
                    return -1;
                else if (charsH[j] == needle.charAt(i) && charsH[j+1] 
                         == needle.charAt(i+1))
            }
        }**/
        

