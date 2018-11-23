class Solution {
    public int romanToInt(String s) {
        if(s == null) return 0;
        int result = 0;
        for(int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if(cur == 'I') {
                result += 1;
            } else if(cur == 'V') {
                result += 5;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'I') {
                    result -= 2;
                }
            } else if(cur == 'X') {
                result += 10;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'I') {
                    result -= 2;
                }
            } else if(cur == 'L') {
                result += 50;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'X') {
                    result -= 20;
                }
            } else if(cur == 'C') {
                result += 100;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'X') {
                    result -= 20;
                }
            } else if(cur == 'D') {
                result += 500;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'C') {
                    result -= 200;
                }
            } else if(cur == 'M') {
                result += 1000;
                if(i - 1 >= 0 && s.charAt(i - 1) == 'C') {
                    result -= 200;
                }
            }
        }
        return result;
    }
}