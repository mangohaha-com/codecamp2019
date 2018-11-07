class Solution {
  public int reverse(int x) {
    int result = 0;
    int newRes = 0;

    while (x != 0) {
      int curDigit = x % 10;
      newRes = 10 * result + curDigit;
      //checkoverflow
      if((newRes - curDigit) / 10 != result)
      return 0;
      result = newRes;
      x = x/10;
    }
    return result;
   }
}