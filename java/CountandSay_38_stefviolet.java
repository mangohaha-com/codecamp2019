class Solution {
    public String countAndSay(int n) {

        if (n <= 0) {
            return "";
        }
        String res = "1";
        if (n == 1) {
            return res;
        }
        while (n-- > 1) {
            StringBuilder sb = new StringBuilder();
            int count = 0;
            char prev = res.charAt(0);
            int i = 0;
            while (i < res.length()) {
                while (i < res.length() && res.charAt(i) == prev) {
                    count++;
                    i++;
                }
                sb.append(count);
                sb.append(prev);
                if (i < res.length()) {
                    prev = res.charAt(i);
                }
                count = 0;
            }
            res = sb.toString();
        }
        return res;
    }
}
