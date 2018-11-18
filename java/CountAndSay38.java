class CountAndSay38 {
    public String countAndSay(int n) {
        if(n == 1) {
            return "1";
        }
        
        String str = countAndSay(n - 1) + "*";
        int count = 1;
        String s = "";
        char[] tmp = str.toCharArray();
        for(int i = 0; i < tmp.length - 1; i++) {
            if(tmp[i] == tmp[i + 1]) {
                count++;
            } else {
                s = s + count + tmp[i];
                count = 1;
            }
        }
        return s;
    }
}