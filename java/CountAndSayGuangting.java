//Time complexity: O(m * n): n is the parameter input, m is the length of the result.
//Space Complexity: O(n), since we have generate n strings;


class CountAndSayGuangting {
    public String countAndSay(int n) {
        //return generateNext(countAndSay(n - 1));
        String cur = "1";
        while(n > 1) {
            String next = generateNext(cur);
            cur = new String(next);
            n--;
        }
        return cur;
    }

    private String generateNext(String s) {
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < s.length();) {
            int count = 0;
            char cur = s.charAt(i);
            int j = i;
            for(; j < s.length(); j++) {
                if(cur == s.charAt(j)) {
                    count++;
                } else {
                    break;
                }
            }
            char[] countCharArray = String.valueOf(count).toCharArray();
            for(char each : countCharArray) {sb.append(each);}
            sb.append(cur);
            i += count;
        }
        return sb.toString();
    }
}
