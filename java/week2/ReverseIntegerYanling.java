class ReverseIntegerYanling {
    public int reverse(int x) {
        if(x==Integer.MIN_VALUE)
            return 0;
        int num = Math.abs(x);
        int res = 0;
        while(num!=0){
            if(res>(Integer.MAX_VALUE-num%10)/10)
                return 0;
            res = res*10+num%10;
            num /= 10;
        }
        return x>0?res:-res;
    }
}

//Time Complexity: O(n)
//Space Complexity: O(1)