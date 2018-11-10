class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> res = new ArrayList<>();
        int i = s.indexOf("++");
        while(i < s.length() && i >=0 ) {
            char[] temp = s.toCharArray();
            temp[i] = '-';
            temp[i+1] ='-';
            res.add(String.valueOf(temp));
            i = s.indexOf("++", i+1);
        }
        return res;
    }
}