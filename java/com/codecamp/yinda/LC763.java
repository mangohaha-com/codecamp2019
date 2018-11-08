package com.codecamp.yinda;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LC763 {

    public static void main(String[] args){
        LC763 lc = new LC763();
        lc.partitionLabels("eaaaabaaec");
    }
    // AC， 38%，时间O(n)，空间O(n)
    // two pointer
    public List<Integer> partitionLabels(String S) {
        List<Integer> indexes = new ArrayList<>();
        if(S==null || S.length()==0){
            return indexes;
        }

        for(int slow = 0 ; slow < S.length(); slow++){
            int lastIndex = getLastChar(S, S.charAt(slow));
            if(lastIndex==slow){
                indexes.add(slow);
                continue;
            }
            Set<Character> set = new HashSet<>();
            set.add(S.charAt(slow));
            for(int i = slow+1 ; i < lastIndex ; i++ ){
                if(set.contains(S.charAt(i))) continue;
                int tempLast = getLastChar(S , S.charAt(i));
                if(tempLast>lastIndex){
                    lastIndex = tempLast;
                }
                set.add(S.charAt(i));
            }
            indexes.add(lastIndex);
            slow = lastIndex;
        }
        List<Integer> ans = new ArrayList<>();
        if(indexes.size()==1){
            ans.add( indexes.get(0)+1 );
        }else{
            ans.add( indexes.get(0)+1 );
            for(int i = 1; i< indexes.size(); i++){
                ans.add( indexes.get(i)-indexes.get(i-1) );
            }
        }
        return ans;
    }

    // 可以优化的地方就是传数组会快点，string操作还是慢
    public int getLastChar(String s, char c){
        int ans = s.length()-1;
        for(; ans >= 0; ans--){
            if(s.charAt(ans) == c){
                return ans;
            }
        }
        return ans;
    }
}
