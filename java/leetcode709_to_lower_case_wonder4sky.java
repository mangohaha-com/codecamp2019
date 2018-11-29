public class leetcode709_to_lower_case_wonder4sky {

    class Solution {
        public String toLowerCase(String str) {

            // turn string to char Array
            char[] ch = str.toCharArray();
            String str1 = null;

            for (int i = 0; i < ch.length; i++) {
                if (ch[i] - 'A' >= 0 && ch[i] - 'A' <= 26) {
                    int n = ch[i] - 'A' + 'a';
                    ch[i] = (char)(n);
                }
            }

            // 要把char array转成一个string，用String.valueOf(charArray);
            str1 = String.valueOf(ch);
            return str1;
        }

    }
}
