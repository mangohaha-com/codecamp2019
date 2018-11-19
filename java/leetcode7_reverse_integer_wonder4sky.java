class Solution {
    public int reverse(int x) {

        if (x == 0)
            return 0;

        int total = 0;
        int new_total = 0;

        //在循环里就要check是不是溢出了
        // total = new_total 这一步很重要；累加或累乘并不是一定要total ＝ total＊ 10
        // 还可以new_total = total * 10  然后做别的操作，然后total = new_total
        // 负数的余数是什么，商是什么？
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