0
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        Map<Character, Integer> intValues = new HashMap<Character, Integer>(){{
            put('I',1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
        
        char[] arr = s.toCharArray();
        int lastDigit = intValues.get(arr[arr.length-1]);
        sum += lastDigit;
        
        for(int i=arr.length-2;i>=0;i--){
            int digit = intValues.get(arr[i]);
            if(digit>=lastDigit)
                sum += digit;
            else
                sum -= digit;
            lastDigit = digit;
        }
        return sum;
	}
}