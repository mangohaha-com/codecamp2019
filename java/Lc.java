package com.company;

import java.util.*;

public class Lc {

    // moving /sliding window
    // indgree topological sort


    /*
    713 subarray-product-less-than-k/
    my solution is to use dp, the Ni = num[i] * all solution of Ni-1, if <k
     */
    public static class Q713 {

        // moving window


        public int solve(int[] nums, int k) {

            int result = 1;
            int left = 0;
            int counter = 0;

            for (int right = 0; right < nums.length; right++) {
                result *= nums[right];

                if (result >= k) {

                    while (result >= k && left <= right) {
                        result /= nums[left];
                        left++;
                    }


                }

                counter += right - left + 1;
            }


            return counter;
        }


    }


    /*
 698. Partition to K Equal Sum Subsets
  */
    public static class Q698 {


        public boolean solve(int[] nums, int k) {

            int sum = 0;
            for (int i = 0; i < nums.length; i++) {
                sum += nums[i];
            }

            if (sum % k != 0) return false;

            int subSum = sum / k;
            for (Integer it : nums) {
                if (it > subSum) return false;
            }

            boolean[] used = new boolean[nums.length];
            for (int i = 0; i < used.length; i++) {
                used[i] = false;

            }

            return helper(nums, subSum, k, used, 0, 0, 0);

        }

        private boolean helper(int[] nums, int subSum, int k, boolean[] used, int index, int currentSum, int numberofItem) {

            if (k == 1) return true;
            if (currentSum == subSum && numberofItem > 0) {
                return helper(nums, subSum, k - 1, used, index, 0, 0);
            }

            for (int i = index; i < nums.length; i++) {

                if (!used[i]) {

                    used[i] = true;
                    if (helper(nums, subSum, k, used, index + 1, currentSum + nums[i], numberofItem + 1)) return true;
                    used[i] = false;


                }

            }

            return false;

        }


    }


    /*
340. Longest Substring with At Most K Distinct Characters
*/
    public static class Q340 {


        // moving window
        public int solve(String input, int k) {

            Map<Character, Integer> freq = new HashMap<>();
            int leftMostPointer = 0;
            int result = Integer.MIN_VALUE;

            for (int right = 0; right < input.length(); right++) {

                if (!freq.containsKey(input.charAt(right))) {
                    freq.put(input.charAt(right), 0);
                }
                freq.put(input.charAt(right), freq.get(input.charAt(right)) + 1);

                if (freq.size() > k) {

                    result = Math.max(result, right - leftMostPointer);

                    // shrink map by moving right the left pointer
                    while (leftMostPointer <= right && freq.size() > k) {

                        if (freq.get(input.charAt(leftMostPointer)) == 1) {
                            freq.remove(input.charAt(leftMostPointer));
                        } else {
                            freq.put(input.charAt(leftMostPointer), freq.get(input.charAt(leftMostPointer)) - 1);
                        }
                        leftMostPointer++;
                    }

                }

            }

            if (leftMostPointer < input.length()) {
                result = Math.max(result, input.length() - leftMostPointer);
            }


            return result;


        }


    }


    /*
926. Flip String to Monotone Increasing
https://blog.csdn.net/qq_17550379/article/details/83270427?utm_source=blogxgwz2
*/
    public static class Q926 {


        public int solve(String input) {

            int onesBefore = 0;
            int zeroBefore = 0;
            int oneTotal = 0;
            int zeroTotal = 0;

            int result = Integer.MIN_VALUE;
            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == '0') {
                    zeroTotal++;
                } else {
                    oneTotal++;
                }
            }

            for (int i = 0; i < input.length(); i++) {

                if (input.charAt(i) == '1') {
                    onesBefore++;
                } else {
                    zeroBefore++;
                }

                result = Math.min(result, onesBefore + zeroTotal - zeroBefore);
            }

            return result;
        }


    }


    /*
    738 monotone-increasing-digits

*/
    public static class Q738 {


        public int solve(int n) {

            if (n == 10) return 9;
            if (n >= 0 && n < 20) return n;

            char[] inputC = String.valueOf(n).toCharArray();

            int leftMostDropPosition = -1;
            for (int i = inputC.length - 2; i >= 0; i--) {
                if (inputC[i] > inputC[i + 1]) {
                    leftMostDropPosition = i;
                    inputC[i]--;
                }
            }

            for (int i = leftMostDropPosition + 1; i < inputC.length; i++) {
                inputC[i] = '9';
            }

            return Integer.valueOf(new String(inputC));
        }


    }


    /*
 163 Missing Ranges
*/
    public static class Q163 {


        public List<String> solve(int[] array, int lower, int upper) {

            List<String> result = new ArrayList<>();

            int index = 0;
            int len = array.length;

            if (array[index] - lower == 2) {
                result.add(String.valueOf(array[index] - 1));
            }


            if (array[index] - lower > 2) {

                String start = String.valueOf(lower + 1);
                String end = String.valueOf(array[index] - 1);
                result.add(start + "->" + end);

            }

            while (index < len - 1) {
                int curent = array[index];
                int next = array[index + 1];

                if (next - curent <= 1) {
                    index++;
                    continue;
                }

                if (next - curent == 2) {
                    result.add(String.valueOf(array[index] + 1));
                    index++;
                    continue;
                }


                if (next - curent > 2) {
                    String start = String.valueOf(curent + 1);
                    String end = String.valueOf(next - 1);
                    result.add(start + "->" + end);
                    index++;
                    continue;
                }

            }


            if (upper - array[index] >= 2) {

                String start = String.valueOf(array[index] + 1);
                String end = String.valueOf(upper);
                result.add(start + "->" + end);

            }


            return result;


        }


    }


    /*
269 Alien Dictionary
*/
    public static class Q269 {


        public String solve(String[] inputs) {

            if (inputs.length <= 1) return "";

            // build map a->b/c/d, and an indegree table
            int[] inDegree = new int[26];
            for (int i = 0; i < inDegree.length; i++) {
                inDegree[i] = 0;
            }

            Map<Character, List<Character>> edges = new HashMap<>();

            for (int i = 0; i < inputs.length - 1; i++) {
                String s1 = inputs[i];
                String s2 = inputs[i + 1];

                for (int j = 0; j < Math.min(s1.length(), s2.length()); j++) {
                    char c1 = s1.charAt(j);
                    char c2 = s2.charAt(j);

                    if (c1 != c2) {

                        inDegree[c2 - 'a']++;
                        if (!edges.containsKey(c1)) {
                            List<Character> tmp = new ArrayList<>();
                            edges.put(c1, tmp);
                        }

                        edges.get(c1).add(c2);
                        break;

                    }

                }

            }

            PriorityQueue<Character> priorityQueue = new PriorityQueue<>();

            Set<Character> allChars = new HashSet<>();
            for (String item : inputs) {
                for (Character c : item.toCharArray()) {
                    allChars.add(c);
                }
            }

            for (Character c : allChars) {
                if (inDegree[c - 'a'] == 0) {
                    priorityQueue.add(c);
                }
            }

            StringBuilder stringBuilder = new StringBuilder();
            while (!priorityQueue.isEmpty()) {
                Character c = priorityQueue.poll();
                stringBuilder.append(c);
                for (Character successor : edges.get(c)) {
                    if (inDegree[successor - 'a'] == 1) {
                        priorityQueue.add(successor);
                    }
                    inDegree[successor - 'a']--;
                }
            }

            return stringBuilder.toString().length() == allChars.size() ? stringBuilder.toString() : "";


        }


    }


}
