package USACO.training.section1_2;

import java.io.*;
import java.util.*;

class ride {
    static int ASCII_OFFSET = 64;
    static int UFO = 47;
    public static PrintWriter out;
    
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("ride.in"));
        out = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
        
        StringTokenizer in = new StringTokenizer(f.readLine());
        String comet = in.nextToken();
        in = new StringTokenizer(f.readLine());
        String group = in.nextToken();
        your_ride_is_here(comet, group);
        out.close();
    }
    
    private static void your_ride_is_here(String comet, String group) {
        int cometVal = 1;
        int groupVal = 1;
        for (char c : comet.toCharArray()) {
            cometVal *= (c - ASCII_OFFSET);
        }
        
        for (char c : group.toCharArray()) {
            groupVal *= (c - ASCII_OFFSET);
        }
        
        if (cometVal % UFO == groupVal % UFO) {
            out.println("GO");
        } else {
            out.println("STAY");
        }
    }
}

/* http://train.usaco.org/usacoprob2?S=ride&a=pUPQq8h2ZMx
 * INPUT
------- test 1 [length 14 bytes] ----
COMETQ
HVNGAT
------- test 2 [length 13 bytes] ----
STARAB
USACO
------- test 3 [length 12 bytes] ----
EARTH
LEFTB
------- test 4 [length 13 bytes] ----
PULSAR
VENUS
------- test 5 [length 12 bytes] ----
KANSAS
UTAH
------- test 6 [length 11 bytes] ----
APPLE
URSA
------- test 7 [length 10 bytes] ----
MSFT
MARS
------- test 8 [length 13 bytes] ----
PLUTO
BKHOLE
------- test 9 [length 13 bytes] ----
COWSBC
RIGHT
------- test 10 [length 14 bytes] ----
DRKMTR
SNIKER
 */
