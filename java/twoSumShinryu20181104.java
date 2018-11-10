import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
/*
DATE:2018-11-04-23:59
AUTHOR: ShinryuLee
PROJECT: codeCAMP2019
-------------------------------------------------------------------
param1: Array of integers
param2: Given Sum Target
Output: Pairs of Indices that would be added up to the target.
--------------------------------------------------------------------
*/

public class twoSumShinryu20181104 {

    //結果メッセージを設置
    private static String INFO_PAIRS_NOT_FOUND = "No pairs!!!!";
    private static String INFO_PAIRS_FOUND = "Pairs are found:";

    //テスト用データを設置
    private static final int[] TEST_ARRAY = {2,5,9,0,1,3,5};
    private static final int TEST_TARGET = 2;

    public static void main (String[] args){
        twoSumShinryu20181104 twoSum = new twoSumShinryu20181104();
        twoSum.processLogic(TEST_ARRAY,TEST_TARGET);
    }

    /* 処理のロジッ�?
    Input: Given array, Given target
    Output: INFO MESSAGE
    */
    private void processLogic(int[] arry, int tar){

        //一時保存用マップを作成,[Key 加数、VALUE 加数のインデックス]
        Map<Integer, Integer> tempMap = new HashMap<>();
        //結果格納用リストを作�?
        List<String> resultPairs = new ArrayList<>();
        //処理ルー�?
        for (int i = 0; i < arry.length; i ++){
            if (tempMap.containsKey(tar - arry[i])){
                resultPairs.add( i +" + "+ tempMap.get(tar - arry[i]));
            }
            tempMap.put(arry[i], i);
        }
        //結果メッセー�?
        if(!resultPairs.isEmpty()){
            System.out.println(INFO_PAIRS_FOUND + resultPairs);
        } else{
            System.out.println(INFO_PAIRS_NOT_FOUND);
        }
    }
}
