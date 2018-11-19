class Solution {
    public String countAndSay(int n) {
        
        String str = "1";
        //StringBuilder temp = new StringBuilder();
        for (int i = 1; i < n; i++) {
            StringBuilder temp = new StringBuilder();
            char[] chars = str.toCharArray(); 
            for (int j = 0; j < chars.length; j++ ) {
                int count = 1;
                while (j < (chars.length -1) && chars[j] == chars[j+1]) {
                    count++; //why not ++count?
                    j++;  // important
                }    
                temp.append(count);
                temp.append(chars[j]);
            }
            str = temp.toString();
        }
        return str;
    }
}