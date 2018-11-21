class sqrtGuangting {
  public int mySqrt(int x) {
    if(x == 0) return 0;

    int left = 0;
    int right = Integer.MAX_VALUE;
    while(left + 1 < right) {
      int mid = left + (right - left) / 2;
      if(x/mid == mid) {
        return mid;
      } else if(x/mid > mid){
        left = mid;
      } else {
        right = mid;
      }
    }
    return left == x/left? left:right;
  }
  public static void main(String[] args) throws IOException {
      int ret = new sqrtGuangting().mySqrt(8);

      String out = String.valueOf(ret);

      System.out.print(out);
    }
}

