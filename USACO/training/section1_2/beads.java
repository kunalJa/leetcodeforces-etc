package USACO.training.section1_2;

import java.io.*;
import java.util.*;

class beads {
    public static BufferedReader f;
    public static PrintWriter out;
    public static StringTokenizer st;
    
    private static void initializeIO(String filename) throws IOException {
        f = new BufferedReader(new FileReader(filename + ".in"));
        out = new PrintWriter(new BufferedWriter(new FileWriter(filename + ".out")));
    }
    
    public static void main(String[] args) throws IOException {
        int N;
        String necklace;
        initializeIO("beads");
        st = new StringTokenizer(f.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(f.readLine());
        necklace = st.nextToken();
        out.println(maxCircularRepeatedBeads(N, (necklace + necklace).toCharArray()));
        out.close();
    }

    private static int maxCircularRepeatedBeads(int N, char[] necklace) {
        // Circular maximum subsequence length of repeated characters where
        // you change which repeats once.
        // e.g. rrrrrbbbrb = 8 -> you can change letters once.
        // Kadane's algorithm?
        if (N <= 2) return N;
        int max = 0;
        int soFar = 0;
        int partialSoFar = 0;
        int numSwaps = 0;
        char currentRepeating = necklace[0];
        int soFarStart = 1;
        boolean w = false;
        int adjustForW = 0;
        int lagState = 0;
        for (int i = 0; i < 2 * N - 1; i++) {
            w = necklace[i] == 'w'; 
            if (!w && necklace[i] != currentRepeating) {
                currentRepeating = necklace[i];
                numSwaps++;
            }
            if (numSwaps == 2) {
                numSwaps = 1;
                soFar = partialSoFar += lagState;
                lagState = adjustForW;
                partialSoFar = 0;
                soFarStart = i;
                adjustForW = 0;
            }
            if (w) {
                adjustForW++;
            } else {
                adjustForW = 0;
            }
            soFar++;
            if (max < soFar) {
                max = soFar;
            }
            if (numSwaps == 1) {
                partialSoFar++;
            }
        }
        return Math.min(N, max);
    }
}

/* http://train.usaco.org/usacoprob2?S=beads&a=CP4behTSyBM
 */
