class Solution {
    public int partitionDisjoint(int[] A) {
        int maxL = A[0];
        int i;
        boolean won = false;
        for (i = 0; i < A.length - 1; i++) {
            won = false;
            maxL = Math.max(A[i], maxL);
            for (int j = i + 1; j < A.length; j++) {
                if (A[j] < maxL) {
                    won = true;
                }
            }
            if (!won) return i + 1;
        }
        return -1;
    }
}