class Solution {
    public int reverse(int x) {
        
        if (x == 0)
            return 0;
        
        int total = 0;
        int new_total = 0;
        
        //??????check??????
        // total = new_total ??????????????????total ? total? 10 
        // ???new_total = total * 10  ??????????total = new_total
        // ??????????????
        while (x != 0) {
            int module = x % 10;
            new_total = total * 10 + module;
            if ((new_total - module)/10 != total) 
                return 0;
            x = x / 10;
            total = new_total;
           
        }
        
        return total;
    }
}