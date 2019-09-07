package USACO.training.section1_2;

import java.io.*;
import java.util.*;

class friday {
    public static BufferedReader f;
    public static PrintWriter out;
    public static StringTokenizer st;
    public static int startYear = 1900;
    private static int startDay = 2;
    private static int[] days = new int[7];
    private static int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    private static void initializeIO(String filename) throws IOException {
        f = new BufferedReader(new FileReader(filename + ".in"));
        out = new PrintWriter(new BufferedWriter(new FileWriter(filename + ".out")));
    }
    
    public static void main(String[] args) throws IOException {
        int N;
        initializeIO("friday");
        st = new StringTokenizer(f.readLine());
        N = Integer.parseInt(st.nextToken());
        daysOf13(N);
        printDaysOf13();
        out.close();
    }

    private static void daysOf13(int n) {
        for (int year = startYear; year < startYear + n; year++) {
            for (int month = 0; month < 12; month++) {
                int numDays = months[month];
                numDays = month == 1 && isLeapYear(year) ? numDays + 1 : numDays;
                days[(startDay + 12) % 7]++;
                startDay = (startDay + numDays) % 7;
            }
        }
    }
    
    private static boolean isLeapYear(int year) {
        if (isCentury(year)) {
            return year % 400 == 0; 
        } else {
            return year % 4 == 0;
        }
    }
    
    private static boolean isCentury(int year) {
        return year % 100 == 0;
    }
    
    private static void printDaysOf13() {
        for (int i = 0; i < days.length - 1; i++) {
            out.print(days[i] + " ");
         }
         out.println(days[days.length - 1]);
    }
}

/* http://train.usaco.org/usacoprob2?a=o3OnbutWqfb&S=friday
 * Compute the frequency that the 13th of each month lands on
 * Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday
 * over a given period of N years.
 * The time period to test will be from January 1, 1900 to
 * December 31, 1900+N-1 for a given number of years, N.
 */
