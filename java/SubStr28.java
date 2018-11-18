class SubStr28 {
    public int strStr(String haystack, String needle) {
        if(haystack == null || needle == null) return -1;
        for(int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            if(haystack.substring(i,i + needle.length()).equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}