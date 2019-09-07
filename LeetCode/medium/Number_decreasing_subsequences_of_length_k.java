/**
 * Return the number of decreasing subsequences of length 3
 */

package LeetCode.medium;

import java.util.List;

public class Number_decreasing_subsequences_of_length_k {
    static long maxInversions(List<Integer> prices) {
        // HashMap<Integer, Integer> lessThan = new HashMap<>();
        // for (Integer i : prices) {
        //     if (!lessThan.containsKey(i)) {
        //         lessThan.put(i, 0);
        //     }
        //     for (Map.Entry<Integer, Integer> visited : lessThan.entrySet()) {
        //         if (i < visited.getKey()) {
        //             visited.setValue(visited.getValue() + 1);
        //             //System.out.println(visited.getKey() + " and i: " + i);
        //         }
        //     }
        // }
        // int count = 0;
        // for (Map.Entry<Integer, Integer> visited : lessThan.entrySet()) {
        //     int n = visited.getValue() - 2;
        //     System.out.println(visited.getKey() + " and n: " + n);
        //     if (n > 0)
        //         count += ((n * (n + 1)) / 2);
        // }
        // return count;
    
        // I wanted to avoid such a bad runtime solution O(n^2), space O(1).
        // I was tinkering with making some sort of graph but I can't quite get it to work.
        long count = 0;
        for (int i = 0; i < prices.size(); i++) {
            long localBigger = 0;
            for (int j = 0; j < i; j++) {
                if (prices.get(j) > prices.get(i)) {
                    localBigger++;
                }
            }
            long localSmaller = 0;
            for (int j = i + 1; j < prices.size(); j++) {
                if (prices.get(j) < prices.get(i)) {
                    localSmaller++;
                }
            }
            count += localBigger * localSmaller;
        }
        return count;
    }
}
