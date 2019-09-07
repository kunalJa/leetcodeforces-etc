/**
 * Given a circular array C of integers represented by A, find the
 * maximum possible sum of a non-empty subarray of C. Here, a circular
 * array means the end of the array connects to the beginning of the array.
 * (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
 * Also, a subarray may only include each element of the fixed buffer
 * A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j],
 * there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
 *  
 *  Example 1:
 *  Input: [1,-2,3,-2]
 *  Output: 3
 *  Explanation: Subarray [3] has maximum sum 3
 *  
 *  Example 2:
 *  Input: [5,-3,5]
 *  Output: 10
 *  Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
 *  
 *  Example 3:
 *  Input: [3,-1,2,-1]
 *  Output: 4
 *  Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
 *  
 *  Example 4:
 *  Input: [3,-2,2,-3]
 *  Output: 3
 *  Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
 *  
 *  Example 5:
 *  Input: [-2,-3,-1]
 *  Output: -1
 *  Explanation: Subarray [-1] has maximum sum -1
 */

package LeetCode.medium;

public class Maximum_sum_circular_subarray {
    public static int maxSubarraySumCircular(int[] A) {
        int len = A.length;
        if (len == 0) return 0;
        int[] B = new int[2 * len - 1];
        for (int i = 0, j = 0; j < 2 * len - 1; j++, i = (i + 1) % len) {
            B[j] = A[i];
        }
       
        int max = B[0];
        int current = B[0];
        int n = B.length;
        int i = 0, j = 1;
        while (i < n && j < n) {
            current += B[j++];
            if (j == i || j > i + len) {
                current -= B[i];
                int temp = j;
                j = i + 1;
                i = temp;
            }
            if (max < current) {
                max = current;
            }
        }
        
        return max;
    }
    
    public static void main(String[] args) {
        int a[] = {5, -3, 5};
        System.out.println(maxSubarraySumCircular(a));
    }
}

/*
 * Time Limit exceeded on below solution.
 * This solution implements Kadane's Algorithm but it is still O(N^2) 
 * 
 *     public int maxSubarraySumCircular(int[] A) {
        int len = A.length;
        int[] B = new int[2 * len - 1];
        for (int i = 0, j = 0; j < 2 * len - 1; j++, i = (i + 1) % len) {
            B[j] = A[i];
        }
       
        int max = B[0];
        int n = B.length;
        for (int j = 0; j <= n - len; j++) {
            if (j > 0 && B[j] < B[j-1]) {
                continue;
            }
            int current = B[j];
            if (max < current) {
                max = current;
            }
            for (int i = j + 1; i < j + len - 1; i++) {
                current = current + B[i];
                if (max < current) {
                    max = current;
                }
                if (current < 0) {
                    current = 0;
                }
            }
        }
        
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += A[i];
        }
        if (max < sum) {
            max = sum;
        }
         
        return max;
    }
 */


/*
 * Time limit exceeded on below solution.
 * A solution that takes time complexity O(N^2):
 * 
        public int maxSubarraySumCircular(int[] A) {
        int limit = A.length;
        int[] B = new int[(A.length * 2) - 1];
        for (int i = 0; i < A.length; i++) {
            B[i] = A[i];
            if (i + 1 != A.length) {
                B[i+A.length] = A[i];
            }
        }
        int max = B[0];
        for (int i = 0; i < limit; i++) {
            int currentSum = 0;
            for (int j = i; j < i + limit; j++) {
                currentSum += B[j];
                if (currentSum > max) max = currentSum;
            }
        }
        return max;
    }
 */