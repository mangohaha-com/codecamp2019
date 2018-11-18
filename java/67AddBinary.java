class Solution {
    public String addBinary(String a, String b) {
        if(a == null || b == null) return a == null ? (b==null ? "" : 
b):a;
        if(a.length() == 0) return b;
        if(b.length() == 0) return a;
        int m = a.length();
        int n = b.length();
        StringBuilder sb = new StringBuilder();
        int flow = 0;
        int i = m-1; int j = n-1;
        while(i >= 0 || j >= 0) {
            int temp = flow;
            flow = 0;
            if(i >= 0) {
                temp += a.charAt(i)-'0';
            }
            if(j >= 0) {
                temp += b.charAt(j)-'0';
            }
            flow = temp/2;
            sb.append(temp%2);
            i--; j--;
        }
        if(flow == 1) {
            sb.append(flow);
        }
        return sb.reverse().toString();
    }
}
