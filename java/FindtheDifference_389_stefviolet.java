class Solution {
    public char findTheDifference(String s, String t) {
        int ascii = 0;
        for (int i = 0; i < s.length(); i++) {
            ascii += (int)t.charAt(i) - (int) s.charAt(i);
        }
        ascii += (int) t.charAt(t.length() - 1);
        return (char) ascii;
    }
}
