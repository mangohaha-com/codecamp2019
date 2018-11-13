//Time complexity: O(m * n)
//Space complexity: O(1)
public class ImplementStrstrGuangting {
    public int strStr(String haystack, String needle) {
        if(haystack == null || needle == null || needle.length() > haystack.length()) {
            return -1;
        }

        for(int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            if(haystack.substring(i, i + needle.length()).equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}
