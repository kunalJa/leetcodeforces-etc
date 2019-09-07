package USACO.training.section1_3;

import java.io.*;
import java.util.*;

class milk2 {
    public static BufferedReader f;
    public static PrintWriter out;
    public static StringTokenizer st;
    
    private static void initializeIO(String filename) throws IOException {
        f = new BufferedReader(new FileReader(filename + ".in"));
        out = new PrintWriter(new BufferedWriter(new FileWriter(filename + ".out")));
    }
    
    private static int longestContinuous(List<Vector2<Integer, Integer>> farmers) {
        int max = farmers.get(0).getSecond() - farmers.get(0).getFirst();
        Vector2<Integer, Integer> current = new Vector2<>(farmers.get(0).getFirst(), farmers.get(0).getSecond());
        for (Vector2<Integer, Integer> farmer : farmers) {
            if (current.compareTo(farmer) == 0)
                continue;
            
            if (current.overlaps(farmer)) {
                if (farmer.getSecond() > current.getSecond()) {
                    current.setSecond(farmer.getSecond());
                } 
            } else {
                max = Math.max(max, current.getSecond() - current.getFirst());
                current = farmer;
            }
        }
        
        return max;
    }
    
    private static int longestIdle(List<Vector2<Integer, Integer>> farmers) {
        int max = 0;
        Vector2<Integer, Integer> current = new Vector2<>(farmers.get(0).getFirst(), farmers.get(0).getSecond());
        for (Vector2<Integer, Integer> farmer : farmers) {
            if (current.compareTo(farmer) == 0)
                continue;
            
            if (current.overlaps(farmer)) {
                if (farmer.getSecond() > current.getSecond()) {
                    current.setSecond(farmer.getSecond());
                }
            } else {
                max = Math.max(max, farmer.getFirst() - current.getSecond());
                current = farmer;
            }
        }
        
        return max;
    }
    
    private static class Vector2<T extends Comparable<? super T>, K extends Comparable<? super K>>
                                implements Comparable<Vector2<T, K>> {
        private T first;
        private K second;
        
        public Vector2() {
            first = null;
            second = null;
        }
        
        public boolean overlaps(Vector2<Integer, Integer> other) {
            if (first instanceof Integer && second instanceof Integer) {
                int f = (Integer) first;
                int s = (Integer) second;
                
                return (f <= other.second && s >= other.first) || (other.first <= s && other.second >= f);
            }
            return false;
        }

        public Vector2(T first, K second) {
            this.first = first;
            this.second = second;
        }

        public T getFirst() {
            return first;
        }

        public K getSecond() {
            return second;
        }

        public void setFirst(T first) {
            this.first = first;
        }

        public void setSecond(K second) {
            this.second = second;
        }
        
        @Override
        public int compareTo(Vector2<T, K> other) {
            if (first.compareTo(other.first) > 0) { // <1, 0> is greater than <0, 200>
                return 1;
            } else if (first.compareTo(other.first) < 0) {
                return -1;
            } else {
                return second.compareTo(other.second); // <1, 2> is greater than <1, 1>
            }
        }
        
        @Override
        public String toString() {
            return first + " " + second;
        }
    }
    
    public static void main(String[] args) throws IOException {
        int N;
        List<Vector2<Integer, Integer>> farmers = new ArrayList<>();
        initializeIO("milk2");
        st = new StringTokenizer(f.readLine());
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(f.readLine());
            farmers.add(new Vector2<Integer, Integer>(Integer.parseInt(st.nextToken()),
                                                      Integer.parseInt(st.nextToken())));
        }
        farmers.sort((o1, o2) -> o1.compareTo(o2)); // Since java-8
        out.print(longestContinuous(farmers) + " ");
        out.println(longestIdle(farmers));
        out.close();
    }
}

/*  http://train.usaco.org/usacoprob2?S=milk2&a=IMaFxV70At0 */

/** This solution for longest cont. is too slow (N^2): given 2 unsorted arraylists of start times and end times
 * 
        int max = Integer.MIN_VALUE;
        
        for (int j = 0; j < N; j++) {
            // longest continuous milking time starting from farmer j
            int currentStart = start.get(j);
            int currentEnd = end.get(j);
           
            // Assumes 1 <= N and end always >= start
            for (int i = 0; i < N; i++) {
                if (start.get(i) < currentStart && (end.get(i) <= currentEnd && end.get(i) >= currentStart))
                    currentStart = start.get(i);
                if (end.get(i) > currentEnd && (start.get(i) >= currentStart && start.get(i) <= currentEnd))
                    currentEnd = end.get(i);
            }
            
            max = Math.max(max, currentEnd - currentStart);
        }

        return max;
 */
