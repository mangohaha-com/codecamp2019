class CountAndSayYanling {
    public String countAndSay(int n) {
        if (n <= 0)
		    return null;
 
	    String init = "1";
        for (int i = 1; i<n; i++) {
            StringBuilder sb = new StringBuilder();
            int count = 1;
            for (int j = 1; j < init.length(); j++) {
                if (init.charAt(j) == init.charAt(j - 1)) {
                    count++;
                } else {
                    sb.append(count);
                    sb.append(init.charAt(j - 1));
                    count = 1;
                }
            }

            sb.append(count);
            sb.append(init.charAt(init.length() - 1));
            init = sb.toString();
        }

        return init;
    }
}
//Time Complexity: O(n)
//Space Complexity: O(1)