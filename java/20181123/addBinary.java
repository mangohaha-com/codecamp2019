class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        int length = Math.max(a.length(), b.length());
        char[] arr = new char[length];
        
        //倒着加
        while(length > 0){
            //截取数字，没有的时候是负数
            int val1 = (i < 0) ? 0 : a.charAt(i--) - '0';
            int val2 = (j < 0) ? 0 : b.charAt(j--) - '0';

            arr[--length] = (char)('0' + (val1 + val2 + carry) % 2);
            carry = (val1 + val2 + carry) / 2;
        }
        String result = new String(arr);

        //进一位
        if(carry == 1)
            result = "1" + result;

        return result;
    }
}